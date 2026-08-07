from flask import Blueprint, request, jsonify, render_template
from app.aws import s3, rekognition, lex, elasticsearch
from app import demo
from config import Config
from datetime import datetime
import json

main = Blueprint('main', __name__)


def _demo_mode():
    return not Config.S3_BUCKET

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', demo_mode=_demo_mode())

@main.route('/search', methods=['GET'])
def search_photos():
    query = request.args.get('q', '')

    if _demo_mode():
        return jsonify(demo.search_demo_photos(query))

    # Use Lex to understand the query
    labels = lex.understand_query(query)

    # Search Elasticsearch
    image_urls = elasticsearch.search_photos(labels)

    return jsonify(image_urls)

@main.route('/upload', methods=['PUT'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    custom_labels = request.form.get('custom_labels', '').split(',')

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if _demo_mode():
        return jsonify({
            "message": "Demo mode: file received but not stored. "
                       "Add real AWS config to enable persistent uploads."
        }), 200

    try:
        # Upload to S3
        s3.upload_file(file, custom_labels)

        # Detect labels with Rekognition
        detected_labels = rekognition.detect_labels(file.filename)

        all_labels = list(set(detected_labels + custom_labels))

        # Index in Elasticsearch
        elasticsearch.index_photo(file.filename, all_labels)

        return jsonify({"message": "File uploaded successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
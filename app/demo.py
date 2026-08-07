import os
import re
import json

_STOPWORDS = {
    "a", "an", "the", "of", "in", "on", "at", "with", "and", "or", "for",
    "to", "show", "me", "find", "search", "photo", "photos", "picture",
    "pictures", "image", "images", "some", "any", "all", "is", "are",
}

_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEMO_DIR = os.path.join(_BASE_DIR, "static", "images", "demo")
_LABELS_FILE = os.path.join(_DEMO_DIR, "labels.json")


def _tokenize(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return {w.rstrip("s") for w in words if w not in _STOPWORDS and len(w) > 1}


def _load_manual_labels():
    if os.path.exists(_LABELS_FILE):
        with open(_LABELS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _list_demo_images():
    if not os.path.isdir(_DEMO_DIR):
        return []
    return sorted(
        f for f in os.listdir(_DEMO_DIR)
        if os.path.splitext(f)[1].lower() in _IMAGE_EXTENSIONS
    )


def _tokens_for(filename, manual_labels):
    labels = manual_labels.get(filename, [])
    name_words = os.path.splitext(filename)[0].replace("-", " ").replace("_", " ")
    return _tokenize(" ".join(labels)) | _tokenize(name_words)


def search_demo_photos(query):
    manual_labels = _load_manual_labels()
    filenames = _list_demo_images()

    query_tokens = _tokenize(query)
    if not query_tokens:
        return [f"/static/images/demo/{f}" for f in filenames]

    scored = []
    for filename in filenames:
        tokens = _tokens_for(filename, manual_labels)
        score = len(query_tokens & tokens)
        if score == 0:
            score = sum(
                1 for qt in query_tokens for t in tokens
                if len(qt) > 2 and (qt in t or t in qt)
            )
        if score > 0:
            scored.append((score, filename))

    scored.sort(key=lambda pair: -pair[0])
    return [f"/static/images/demo/{filename}" for _, filename in scored]

# Smart Image Gallery #

Text-based Image content Search application built as part of the course CS-GY 9223 Cloud Computing at New York University.

## Usage ##

1. Clone the repository.
2. Provision the foollowing resources on AWS:
 - S3 bucket
 - elasticsearch domain
 - MongoDb database
 - Rekognition
 - Lex bot
3. Setup Lex bot to identify keywords from queries with relevant intents and slots.
4. Setup DynamoDB and ElasticSearch to query and serve the recommendations.
5. Update ```config.py``` file with your credentials. 
6. To test locally run ```docker compose up```
7. To deploy to Kubernetes cluster run the following commands
``` 
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
```

## Tech Stack ##
- Python / Flask 
- Javascript
- AWS S3
- AWS Lex
- Elasticsearch
- DynamoDb
- Docker
- Kubernetes
- Prometheus

## UI ##
<img src="https://github.com/Safdarahmedd/smart-image-gallery/blob/main/images/application-browser.png" alt="Image Search UI" width="600"/>
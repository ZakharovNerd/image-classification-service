## About the project

This project project consists of Machine Learning service for multilabel image classification task, created with **FastAPI** and dependency-injector for greater readability and testing. The model training is done in another repository. The project is managed by **Docker**, the model weights are downloaded by **dvc**, the server part in maintained by **Ansible**

### Goal

The main purpose of this project is to obtain more practice and knowledge about building ML application with FastApi framework connected with several services in docker.

### Dataset & model

The task is defined as the multi-label-classification problem. The chosen CNN model consists of the base model, which is pre-trained VGG16 network and head model - Sequential model composed of FeedForward Neural Networks

The data for training we are using are taken from [Planet: Understanding the Amazon from Space Kaggle competition](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space). More info can be found at the competition website. In a nutshell we want to label satellite image chips with atmospheric conditions and various classes of land cover/land use. It is a multi-labeling problem with 17 different classes. In the competition algorithms were scored using the mean F2 score.

Here we only use the jpg images. 

## Functionality

### 1.a) Starting app on docker
To start the application we can simply run (being located in project dir) in terminal:

`docker build -f Dockerfile . --force-rm=true -t $(DOCKER_IMAGE):$(DOCKER_TAG)`

or using make"

`make build`

And then run the docker image by running:

`docker run --name my-container -p 8000:5000  (DOCKER_IMAGE):$(DOCKER_TAG)`

After docker build and docker run we should see then logs of started service. The API should be accessible on localhost with port 8000 (check logs), e.g. http://0.0.0.0:8000.

### 1.b) Starting the app with python

To start the application without docker we can run:

`python3 -m uvicorn app:app --reload --host='0.0.0.0' --port=8000`

### 2) API Walkthrough
To simply test the api functionality we can use documentation: http://0.0.0.0:8000/docs, check the endpoint and execute Try it out

### 3) Upload image
The endpoint for creating new image object is available through: http://0.0.0.0:8000/classifier/predict. 

### Example response:

{
  "result": [
    "agriculture",
    "clear",
    "habitation",
    "primary",
    "road"
  ]
}

By design, the class is listed only if corresponding probability of a class is greated than 0.2

### 4) Making predictions
To start making predictions:

1. Go on http://0.0.0.0:8000/docs
2. Check classifier/predict endpoint and click Try it out button.
3. Enter the image that was already uploaded.
4. Click Execute and check the response.

### Server

If the server is still running, you can access it through

http://91.206.15.25:1497/


To-do:
описать в readme:
- Как запустить тесты
CI:

- Тесты (юнит и интеграционные)

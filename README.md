
# Air Pressure System(APS) Failure Prediction


The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed
air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of
using an APS instead of a hydraulic system are the easy availability and long-term sustainability of
natural air.
This is a Binary Classification problem, in which the affirmative class indicates that the failure was
caused by a certain component of the APS, while the negative class indicates that the failure was
caused by something else.


# Deployment 

The project is deployed on AWS using Docker. The Docker image is stored in an ECR (Elastic Container Registry) repository. The deployment is fully automated using a CI/CD pipeline.

# Mlops

MLOps is used to automate and streamline the machine learning workflow. The project uses Airflow to schedule batch predictions and training pipelines. The trained model is stored in an S3 bucket.

# Dataset Link

https://archive.ics.uci.edu/dataset/421/aps+failure+at+scania+trucks
## Run Locally

Clone the project

```bash
    git clone https://github.com/kunalshelke90/livesensor.git
```

Go to the project directory

```bash
    cd livesensor
```

Create a virtual environment and install dependencies:

```bash
    conda create -p myenv python=3.8 -y
```


```bash
   conda activate myenv
```
```bash
    pip install -r requirements.txt
```
## Usage
1. Start the Fast API application:

```bash
    python main.py
```
2. Access the application:
Open your web browser and go to http://localhost:8080 to interact with the application. or http://127.0.0.1:8080

## Docker

Docker is used to create a containerized version of the project that can be easily deployed and run on any machine. The Docker container includes all the necessary dependencies and libraries needed to run the project.

1. Build the Docker image:
```bash
    docker build -t livesenor .
```
2. Run the Docker container:
```bash
    docker run -p 5000:5000 livesenor
```
3. Access the application:
Open your web browser and go to http://localhost:5000

## Create ".env" file
```bash
AWS_ACCESS_KEY_ID: The AWS access key ID for your AWS account.
AWS_SECRET_ACCESS_KEY: The AWS secret access key for your AWS account.
AWS_REGION: The AWS region where you will be deploying your application.
AWS_ECR_LOGIN_URI: The URI used to login to the Elastic Container Registry.
ECR_REPOSITORY_NAME: The name of the Elastic Container Registry repository where the Docker image will be pushed.
BUCKET_NAME: The name of the S3 bucket where the trained model and prediction results will be stored.
MONGO_DB_URL: The URL of the MongoDB database used in the project.
```
# License

This project is licensed under the MIT License. See the LICENSE file for details


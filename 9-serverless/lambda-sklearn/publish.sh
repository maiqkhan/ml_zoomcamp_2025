
ECR_URL=334185578767.dkr.ecr.ca-central-1.amazonaws.com
REPO_URL=${ECR_URL}/churn-prediction-lambda
LOCAL_IMAGE=churn-prediction-lambda

docker build -t ${LOCAL_IMAGE} .
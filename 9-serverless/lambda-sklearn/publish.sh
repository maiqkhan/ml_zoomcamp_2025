
ECR_URL=334185578767.dkr.ecr.ca-central-1.amazonaws.com
REPO_URL=${ECR_URL}/churn-prediction-lambda
LOCAL_IMAGE=churn-prediction-lambda


aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin ${ECR_URL}

REMOTE_IMAGE_TAG="${REPO_URL}:v1"

docker build -t churn-prediction-lambda .
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}

echo "Published image to ${REMOTE_IMAGE_TAG}"
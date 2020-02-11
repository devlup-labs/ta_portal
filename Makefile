BUILD_NAME=ta-portal
BUILD_TAG=$$(git log -1 --pretty=%h)

build:
	@docker build -t ${BUILD_NAME}-backend:${BUILD_TAG} -t ${BUILD_NAME}-backend:latest -f Dockerfile .
	@docker build -t ${BUILD_NAME}-frontend:${BUILD_TAG} -t ${BUILD_NAME}-frontend:latest -f frontend/Dockerfile frontend

.env:
	@cp .env.example .env

dev-start: .env
	@docker-compose up -d

dev-stop:
	@docker-compose down
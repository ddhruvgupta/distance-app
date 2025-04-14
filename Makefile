# Variables
REGISTRY = docker.io/ddhruvgupta
FLASK_IMAGE ?= distance-flask
FRONTEND_IMAGE ?= distance-frontend
TAG ?= latest

# Build images using docker-compose
build:
	docker compose build

# Push images to Docker registry
push:
	docker push $(REGISTRY)/$(FLASK_IMAGE):$(TAG)
	docker push $(REGISTRY)/$(FRONTEND_IMAGE):$(TAG)

# Convenience target to build, tag, and push
release: TAG ?= latest
release: build push
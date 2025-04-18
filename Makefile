# Variables
REGISTRY = docker.io/ddhruvgupta
FLASK_IMAGE ?= distance-flask
FRONTEND_IMAGE ?= distance-frontend
VERSION ?= latest

# Build images using docker-compose
build:
	docker compose build

# Push images to Docker registry
push:
	docker push $(REGISTRY)/$(FLASK_IMAGE):$(VERSION)
	docker push $(REGISTRY)/$(FRONTEND_IMAGE):$(VERSION)

# Convenience target to build, tag, and push
release: build tag push
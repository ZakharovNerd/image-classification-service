APP_PORT := 5000
DOCKER_TAG := latest
DOCKER_IMAGE := classification

DEPLOY_HOST := demo_host
KEY_FILE := ~/.ssh/id_rsa
DVC_REMOTE_NAME := my_remote
USERNAME := n.zakharov

.PHONY: run_app
run_app:
	python3 -m uvicorn app:app --reload --host='0.0.0.0' --port=$(APP_PORT)

.PHONY: install
install:
	pip install --no-cache-dir -r requirements.txt

.PHONY: install_dvc
install_dvc:
	pip install pygit2==1.10.1 pathspec==0.9.0
	pip install dvc[ssh]==2.5.4

.PHONY: init_dvc
init_dvc:
	cd weights
	dvc init --no-scm
	dvc remote add --default $(DVC_REMOTE_NAME) ssh://91.206.15.25/home/$(USERNAME)/dvc_files
	dvc remote modify $(DVC_REMOTE_NAME) user $(USERNAME)
	dvc config cache.type hardlink,symlink
	cd ..

.PHONY: download_weights
download_weights:
	cd weights
	dvc pull
	cd ..

.PHONY: lint
lint:
	flake8 src/

.PHONY: build
build:
	docker build -f Dockerfile . --force-rm=true -t $(DOCKER_IMAGE):$(DOCKER_TAG)

.PHONY: deploy
deploy:
	ansible-playbook -i deploy/inventory.ini  deploy/deploy.yml \
		-e host=$(DEPLOY_HOST) \
		-e docker_image=$(DOCKER_IMAGE) \
		-e docker_tag=$(DOCKER_TAG) \
		-e docker_registry_user=$(CI_REGISTRY_USER) \
		-e docker_registry_password=$(CI_REGISTRY_PASSWORD) \
		-e docker_registry=$(CI_REGISTRY) \
		--key-file ${KEY_FILE}

.PHONY: destroy
destroy:
	ansible-playbook -i deploy/inventory.ini deploy/destroy.yml \
		-e host=$(DEPLOY_HOST)


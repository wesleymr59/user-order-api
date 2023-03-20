DOCKER_COMPOSE = docker-compose
#habilitar todos os containers
up-user-api:
	$(DOCKER_COMPOSE) -f user-api/docker-compose.yml up -d

up-order-api:
	$(DOCKER_COMPOSE) -f order-api/docker-compose.yml up -d

up-data-bases:
	$(DOCKER_COMPOSE) -f docker-compose.yml up -d

up-all:
	make up-user-api & make up-order-api & make up-data-bases


#fechar todos os containers
down-user-api:
	$(DOCKER_COMPOSE) -f user-api/docker-compose.yml down --volumes

down-order-api:
	$(DOCKER_COMPOSE) -f order-api/docker-compose.yml down --volumes

down-data-bases:
	$(DOCKER_COMPOSE) -f docker-compose.yml down --volumes
    
down-all:
	make down-user-api & make down-order-api & make down-data-bases
build:
	docker-compose up -d --build

down:
	docker-compose down

reboot:
	docker-compose down
	docker-compose up -d --build

interactive:
	docker-compose exec anaconda bash
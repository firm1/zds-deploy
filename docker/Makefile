zds-build-lite:
	docker-compose -f docker-compose-lite.yml build --force-rm --no-cache

zds-build-full:
	docker-compose build --force-rm --no-cache

zds-stop:
	docker-compose down -v --remove-orphans

zds-start-lite: zds-stop
	docker-compose -f docker-compose-lite.yml up

zds-start-full: zds-stop
	docker-compose -f docker-compose.yml up
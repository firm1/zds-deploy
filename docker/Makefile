zds-build-lite:
	docker-compose build -f docker-compose-lite.yml --force-rm --no-cache

zds-build-full:
	docker-compose build --force-rm --no-cache

zds-stop:
	docker-compose down -v

zds-start-lite: zds-stop
	docker-compose -f docker-compose-lite.yml up

zds-start-full: zds-stop
	docker-compose -f docker-compose.yml up
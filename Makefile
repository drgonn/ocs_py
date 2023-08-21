
install:
	pip install -r requirements.txt

pkg:
	pip freeze > requirements.txt 

run:
	flask --app manage run --debug --host 0.0.0.0 --port 38086

mycommand:
	flask --app  manage mycommand

shell:
	flask --app  manage shell

redis:
	docker exec -it redis_ocs redis-cli

worker:
	celery -A manage.celery worker --loglevel=info
beat:
	celery -A manage.celery beat --loglevel=info
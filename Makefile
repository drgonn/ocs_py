
install:
	pip install -r requirements.txt

pkg:
	pip freeze > requirements.txt 

run:
	flask --app manage run --debug --host 0.0.0.0 --port 38086

mycommand:
	flask --app  manage mycommand

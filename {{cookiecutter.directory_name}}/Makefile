name:={{cookiecutter.directory_name}}/{{cookiecutter.file_name}}

all:
	docker build -t $(name) .
run:
	docker run --rm -p 5050:5050 -p 8080:8080 $(name) -g 5050 -h 8080 -w 2
format:
	isort .
	black .

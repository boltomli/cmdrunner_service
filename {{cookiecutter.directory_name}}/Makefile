name:={{cookiecutter.directory_name}}/{{cookiecutter.file_name}}

all:
	docker build -t $(name) .
run:
	docker run --rm -p 555:555 $(name) -g 555 -w 5
format:
	isort .
	black .

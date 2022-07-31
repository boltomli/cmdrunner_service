FROM python:3.10

WORKDIR /app
COPY requirements.txt ./
RUN ["pip", "install", "-U", "--no-cache-dir", "-r", "requirements.txt"]

COPY *.py ./
ENTRYPOINT ["homi", "run", "{{cookiecutter.file_name}}.py"]

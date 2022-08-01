#!/bin/bash

grpc=5555
http=8888
worker=2

while getopts g:h:w: flag
do
  case "${flag}" in
    g) grpc=${OPTARG} ;;
    h) http=${OPTARG} ;;
    w) worker=${OPTARG} ;;
    *) echo "usage: $0 [-g grpc_port] [-h http_port] [-w worker_num]" >&2
     exit 1 ;;
   esac
done

homi run {{cookiecutter.file_name}}_grpc.py -p ${grpc} -w ${worker} &
uvicorn {{cookiecutter.file_name}}_http:app --host=0.0.0.0 --port=${http} --workers=${worker} &

wait -n
exit $?

#!/bin/sh
cd /usr/src/app
exec gunicorn --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 main:app
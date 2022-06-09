#!/bin/sh
gunicorn --workers=4 --threads=2  -b :$PORT "run:run_server()"
#gunicorn --workers=4 --threads=2  -b :5001 "run:run_server()"
#!/bin/bash

sudo gunicorn -w 2 -b 0.0.0.0:80 s3_logger:app -D -u ubuntu -g ubuntu


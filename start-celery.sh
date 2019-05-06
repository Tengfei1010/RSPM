#!/usr/bin/env bash

./venv/bin/celery worker -A rspm.tasks.celery --loglevel=info
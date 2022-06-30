#!/usr/bin/bash
poetry run coverage erase && \
	poetry run coverage run --source src -m pytest && \
	poetry run coverage html -d html/coverage && \
	poetry run coverage report -m

#!/bin/bash

python manage.py dumpdata --indent=2 > initial_data.json

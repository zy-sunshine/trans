#!/bin/bash

mysql -utrans -ptrans -e "drop database trans;"
mysql -utrans -ptrans -e "create database trans;"
echo Databases:
mysql -utrans -ptrans -e "show databases;"
echo Tables of trans:
mysql -utrans -ptrans trans -e "show tables;"

#yes 'yes' yes 'admin' yes 'admin@example' yes 'admin' yes 'admin' | python manage.py syncdb
#yes 'yes' | python manage.py syncdb
#python manage.py dumpdata --indent=2 auth > initial_data.json
#python manage.py syncdb --noinput
python manage.py syncdb

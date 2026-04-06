#!/bin/sh

set -e

python scr/manage.py migrate

python scr/manage.py runserver
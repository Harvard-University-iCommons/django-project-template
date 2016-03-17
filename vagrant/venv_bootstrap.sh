#!/bin/bash
# Set up virtualenv and migrate project
export HOME=/home/vagrant
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -a /home/vagrant/{{ project_name }} -r /home/vagrant/{{ project_name }}/{{ project_name }}/requirements/local.txt {{ project_name }} 
workon {{ project_name }}
python manage.py migrate

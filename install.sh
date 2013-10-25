#!/bin/bash

clear

echo "Install Street Faces"
echo "Install virtualenv"
apt-get install python-virtualenv
echo "Create new virtualenv"
virtualenv --python=python2.7 --no-site-packages env
echo "virtualenv activate"
source env/bin/activate
echo "Install django"
pip install django
echo "Install python-dev"
apt-get install python-dev
echo "Install PIL"
pip install PIL
echo "Install Selenium"
pip install selenium

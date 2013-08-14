#!/bin/bash

clear

echo "Install Street Faces"
echo "Install virtualenv"
apt-get install python-virtualenv
mkdir street_faces
cd street_faces
echo "Create new virtualenv"
virtualenv --python=python2.7 --no-site-packages env
echo "virtualenv activate"
source env/bin/activate
echo "Install django"
pip install django
echo "Install python-dev"
pip install python-dev
echo "Install PIL"
pip install PIL
[requirements]
python 2.7
python-dev
PIL
django 1.5

[configuration]
DB: sqlite
Naeme: street_faces.sqlite

[installation]
apt-get install python-virtualenv
mkdir street_faces
cd street_faces
virtualenv --python=python2.7 --no-site-packages env
. env/bin/activate
pip install django
pip install python-dev
pip install PIL

[development]
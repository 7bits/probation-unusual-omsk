Requirements
------------
* OS based on Debian
* Python 2.6
* MySQL
* Nginx
* Supervisor

Configuration
-------------
change in settings.py <coed>DEBUG = True</coed> to <code>DEBUG = False</code>
<pre><code>
	$ ./manage.py syncdb
</code></pre>

Installation
------------
Create virtual environment, install required packages::
<pre><code>$ ./install.sh</code></pre>
Also this command can be used for updating.

Development
-----------
Create the tables in the database::
<pre><code>$ ./manage.py syncdb</code></pre>
Run the development server::
<pre><code>$ ./manage.py runserver</code></pre>

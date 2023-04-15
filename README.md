<h1>Bank security console</h1>
<em>This is an educational project.</em>
<h2>How to install</h2>
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

<code>pip install -r requirements.txt</code>

Setup environment variables:
<ol>
<li>Database config:</li>
<ul>
<li>DATABASE_ENGINE (for example, <code>export DATABASE_ENGINE=django.db.backends.postgresql_psycopg2</code>)</li>
<li>DATABASE_HOST</li>
<li>DATABASE_PORT</li>
<li>DATABASE_NAME</li>
<li>DATABASE_USER</li>
<li>DATABASE_PASSWORD</li>
</ul>
<li>DEBUG (default <em>False</em>)</li>
<li>SECRET_KEY (default <em>REPLACE_ME</em>)</li>
<li>ALLOWED_HOSTS (default <em>["*"]</em>)</li>
</ol>

Run project:
<code>python manage.py runserver host:port</code>

<h3>Project Goals</h3>

The code is written for educational purposes on online-course for web-developers dvmn.org.
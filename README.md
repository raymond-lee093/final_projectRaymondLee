# final_projectRaymondLee

Run the collectstatic management command:
python manage.py collectstatic
This will copy all files from your static folders into the STATIC_ROOT directory.


Used for icon images used
https://fonts.google.com/icons

Django Github docs
https://github.com/django/django/tree/main



Created a new custom user model which means that basic users of project are being built differently
and superusers are being built differently.
It is best to clear out the database and recreate a new superuser so database can run smoothly

Interact with Postgres from terminal
To use command line tools (like psql) from your Terminal, add Postgres.app’s bin folder to your $PATH:

You can do this with the following command:

sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp

Login with postgres user with highest privileges:
command: psql postgres postgres

Create new user
command: CREATE USER django WITH PASSWORD '1234'(can create own password);

Verify user creation:
command: \du

Verify created databases:
command: \l

Drop the database that is in current use in project which will clear the data
command: DROP DATABASE databasename;

Verify created databases: (see if database was deleted)
command: \l

Create the database again
command: CREATE DATABASE databasename;

Verify created database:
command: \l

Finally, execute the “GRANT ALL PRIVILEGES” command to grant all the database privileges to the user, 
such as creating a database.
command: GRANT ALL PRIVILEGES ON databasename TO django;

to stop interacting with postgres 
command: "\q"



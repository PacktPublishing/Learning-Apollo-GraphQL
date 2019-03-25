# Project
This sub project is part of the "PackT - Learning Apollo GraphQL" Course.
The project is divided in two folders: Server and Client folders.

**This folder is the 'server' part of the project. **

## Technologies
The 'requirements.txt' contains all the dependencies utilized by python.

This part of the project is to be started prior to the 'client' sub project otherwise the 'client' project will not execute.

## Install MySQL
sudo apt install mysql-server

### Configure MySQL for root privileges
$ sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

### Create Database and assign permissions to root
mysql> CREATE USER 'local_admin'@'localhost' IDENTIFIED BY 'la';
mysql> CREATE DATABASE lagql_demo;
mysql> GRANT ALL PRIVILEGES ON lagql_demo . * TO 'local_admin'@'localhost';

### Restart MySQL
$ service mysql restart

## Setup
Follow the steps below in order to get the GraphQL Server configured.

### Install the packages
sudo apt install python3
sudo apt install python3-pip
sudo apt install ipython
sudo apt install python3-flask
sudo apt-get install python3-pymysql

### Install the packages for the project
pip3 install flask
pip3 install graphene
pip3 install flask-graphql
pip3 install flask-sqlalchemy
pip3 install gunicorn
pip3 install smart_getenv
pip3 install graphene
pip3 install graphene-sqlalchemy
pip3 install flask-cors
pip3 install IPython

### Create the database named "lagql-demo"
python3 shell.py
> db.create_all()
> exit

## Starting the GraphQL Server
Navigate to the folder containing the code
### Sets the location of the python application
export FLASK_APP=lagql_app/app.py
### Assigns the port and begins serving GraphQL via Flask
flask run --reload --port 5000
### The URL for GraphQL will be indicated by flask
Navigate with your browser towards the indicated URL by Flask to execute queries in GraphQL

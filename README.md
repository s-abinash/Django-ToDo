# Django-Todo App
A web app built on the Django framework and MySQL database to store todo lists.


[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

# Requirements
* Python (3.4+)
* Django
* mysql-server

# Usage
#### Install pip3
```sudo apt-get install python3-pip```
#### Install django
```sudo pip3 install django```
#### Install mysql-server
```sudo apt-get install mysql-server```

Change your mysql-server password in [settings.py](django_todo/settings.py)
#### Install python3 client for MySQL
```sudo apt-get install python3-mysqldb```
#### Start mysql in terminal to CREATE a database named todolist
* ```sudo mysql -u root -p```
* ```CREATE DATABASE todolist;```
#### Create table inside the database
```python3 manage.py migrate```
#### Run the app using the following command:
```python3 manage.py runserver```


Navigate to **localhost://8000** on your favourite browser to see the app in action.




# Logs Analysis Project

### Overview

- In this project I was tasked to create a reporting tool which can print reports based on real world web-application data, with fields representing informaton that a webserver would record, such as status codes and URL paths. This reporting tool uses the Python program using psycopg2 module to connect the database.

#### The database includes three tables:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

### Questions:

- What are the most popular three articles of all time? 

- Who are the most popular article authors of all time? 

- On which days did more than 1% of requests lead to errors? 

### Requirements:

- Python 3.6.2

- psycopg2

- PSQL

- Vagrant

- VirtualBox

### How to run:

- Set up VM with vagrant up, then vagrant ssh.

- logs data can be downloaded here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

- load the data onto the database

- psql -d news -f newsdata.sql

- connect to the database

- run python3 logs.py

### Output:

![SS.jpg](https://github.com/iperun/Logs-Analysis-Project/blob/master/SS.JPG)

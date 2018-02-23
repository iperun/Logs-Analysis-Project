Logs Analysis Project

Questions:


What are the most popular three articles of all time? 

Who are the most popular article authors of all time? 

On which days did more than 1% of requests lead to errors? 

Requirements:

Python 3.6.2

psycopg2

PSQL

How to run:

Set up VM with vagrant up, then vagrant ssh.

logs data can be downloaded here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

load the data onto the database

psql -d news -f newsdata.sql

connect to the database

run python3 logs.py

#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

query1 = """ SELECT title, COUNT(log.id) AS views
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
            GROUP BY articles.title ORDER BY views desc LIMIT 3; """

query2 = """ SELECT authors.name, COUNT(articles.author) AS views
            FROM articles, log, authors
            WHERE log.path = CONCAT('/article/', articles.slug)
            AND articles.author = authors.id
            GROUP BY authors.name ORDER BY views desc; """

query3 = """ SELECT *
            FROM (select date(time), ROUND (100.0 * sum (CASE log.status
            WHEN '200 OK' THEN 0 else 1 end)
            /COUNT (log.status), 3) AS error FROM log
            GROUP BY date(time)
            ORDER BY error desc) AS subq WHERE error > 1; """


def Most_Popular_Articles(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query1)
    results = cursor.fetchall()
    for result in results:
        print('\t' + str(result[0]) + " - " + str(result[1]) + " views ")
    db.close()


def Most_Popular_Authors(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query2)
    results = cursor.fetchall()
    for result in results:
        print('\t' + str(result[0]) + " - " + str(result[1]) + " views ")
    db.close()


def Percent_Error(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query3)
    results = cursor.fetchall()
    for result in results:
        print('\t' + str(result[0]) + " - " + str(result[1]) + " % ")
    db.close()


print("Most Popular Articles:")
Most_Popular_Articles(query1)
print("Most Popular Authors:")
Most_Popular_Authors(query2)
print("More than 1 Percent Error:")
Percent_Error(query3)

#!/usr/bin/env python3

import psycopg2


def print_top_articles(dbname, query):
    """Prints out the top 3 articles of all time."""
    db = psycopg2.connect('dbname={}'.format(dbname))
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    question = 'What are the most popular three articles of all time?'
    print(question)
    for row in results:
        print(row[0], '-', row[1], 'views')
    db.close()

def print_top_authors(dbname, query):
    """Prints a list of authors ranked by article views."""
    db = psycopg2.connect('dbname={}'.format(dbname))
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    question = 'Who are the most popular article authors of all time?'
    print(question)
    for row in results:
        print('Author:', row[0], '-', row[1], 'views')
    db.close()



def print_errors_over_one(dbname, query):
    """Prints out the days where more than 1% of requests were errors."""
    db = psycopg2.connect('dbname={}'.format(dbname))
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    question = 'On which days did more than 1% of requests lead to errors?'
    print(question)
    for row in results:
        print('Date:', row[0], 'Error ratio:', '{0:.2f}%'.format(row[1]))
    db.close()


if __name__ == '__main__':
    query_1 = """
    SELECT title, count(*) AS accesses FROM articles JOIN
    log ON concat('/article/', articles.slug) = log.path
    WHERE log.status = '200 OK'
    GROUP BY log.path, articles.title ORDER BY accesses DESC limit 3;
    """

    query_2 = """
    SELECT authors.name, count(*) AS accesses FROM articles JOIN
    authors ON articles.author = authors.id join log ON
    CONCAT('/article/', articles.slug) = log.path WHERE
    log.status = '200 OK' GROUP BY authors.name ORDER BY accesses DESC;
    """

    query_3 = """
    SELECT table1.day,(table2.hits * 100.0)/(table1.hits) AS error_ratio FROM
    ((SELECT DATE(log.time) AS day, count(*) AS hits FROM log GROUP BY day)
    AS table1 JOIN (SELECT DATE(time) AS day, count(*) AS hits FROM log
    WHERE status = '404 NOT FOUND' GROUP BY day) AS table2 ON
    table1.day = table2.day) WHERE (table2.hits * 100.0)/(table1.hits) > 1;
    """


    dbname = 'news'
    print_top_articles(dbname, query_1)
    print_top_authors(dbname, query_2)
    print_errors_over_one(dbname, query_3)

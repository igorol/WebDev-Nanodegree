import psycopg2


def print_result(question, result):
    print(question)
    for row in result:
        print(row[0], row[1])


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


db = psycopg2.connect('dbname=news')
c = db.cursor()
c.execute(query_1)
result1 = c.fetchall()
c.execute(query_2)
result2 = c.fetchall()
c.execute(query_3)
result3 = c.fetchall()

print_result('What are the most popular three articles of all time?', result1)
print_result('Who are the most popular article authors of all time?', result2)
print_result('On which days did more than 1% of requests lead to errors?',
             result3)
#! /usr/bin/env python

import psycopg2

DBNAME = "news"

# Here we query the db to get the answer to question 1
#  What are the most popular three articles of all time?

mostPopularArticles = """
        SELECT articles.title, COUNT(*) AS num FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title ORDER BY num DESC LIMIT 5;
        """

# Here we query the db to get the answer to question 2
# Who are the most popular article authors of all time?

mostPopularAuthors = """
        SELECT authors.name, COUNT(*) AS num FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name ORDER BY num DESC LIMIT 5;
        """


# Here we query the db to get the answer to question 3
# On which days did more than 1% of requests lead to errors?

daysWithMoreErrors = """
        SELECT total.day,
        ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (SELECT date_trunc('day', time) "day", count(*) AS error_requests
        FROM log WHERE status LIKE '404%'
        GROUP BY day) AS errors
        JOIN (
        SELECT date_trunc('day', time) "day", count(*) AS requests
        FROM log
        GROUP BY day) AS total ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
        """

# Lets connect to the and query db to get results


def getQueryResults(sql_query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print ("Unable to connect to the database: " + e)
    else:
        c = db.cursor()
        c.execute(sql_query)
        results = c.fetchall()
        db.close()
        return results


# Here we will find and then print the answer to question 1
mostPopArticlesAre = getQueryResults(mostPopularArticles)

print('\nQuestion 1:')
print('\tWhat are the most popular three articles of all time?')
print('Answer:')
for article in mostPopArticlesAre:
    title = article[0]
    views = str(article[1])
    print("\t\"" + title + " \" - was viewed " + views + " times")

# Here we will find and then print the answer to question 2
mostPopularAuthors = getQueryResults(mostPopularAuthors)
print('\nQuestion 2:')
print('\tWho are the most popular article authors of all time?')
print('Answer:')
for author in mostPopularAuthors:
    title = author[0]
    views = str(author[1])
    print("\t" + title + " - was viewed " + views + " times")

# Here we will find and then print the answer to question 3
print('\nQuestion 3:')
print('\tOn which days did more than 1% of requests lead to errors?')
print('Answer:')
daysWithMoreErrors = getQueryResults(daysWithMoreErrors)
for day in daysWithMoreErrors:
    date = day[0].strftime('%B %d, %Y')
    errors = str(round(day[1]*100, 1)) + "%"
    print("\tOn "+date + " - " + errors + " requests lead to errors\n")

#!/usr/bin/env python3

import psycopg2

# sets DB equal the connection
DB = psycopg2.connect("dbname=news")

# cursor later used to execute the queries
cursor = DB.cursor()


def first_question():
    """first_question prints out the top three articles of all time."""

    print('\nThe most popular three articles of all time:')

    print('-'*25)

    # executes the query.
    cursor.execute("""select articles.title, count(log.path) as views
                      from articles, log
                      where log.path LIKE concat('%', articles.slug)
                      group by articles.title
                      order by views desc
                      limit 3"""
                   )

    results = cursor.fetchall()

    # The for loop prints out the result as a numbered list.
    for row in results:
        print("\"{0}\" -- {1} views".format(row[0], row[1]))


def second_question():
    """This function prints out names and all time views of most polular
        authors."""

    print('\nThe most popular article authors of all time:')

    print('-'*25)

    cursor.execute("""select authors.name, count(log.path) as views
                      from authors, articles, log
                      where authors.id = articles.author
                      and log.path LIKE concat('%',articles.slug)
                      group by authors.name
                      order by views desc;"""
                   )
    results = cursor.fetchall()

    # The for loop prints out the result as a numbered list.
    for row in results:
        print("\"{0}\" -- {1} views".format(row[0], row[1]))


def third_question():
    """ This function prints out days on which there were more
        than 1% errors."""

    print('\nOn days more than 1% of requests lead to errors:')

    print('-'*25)

    cursor.execute("""select *
                      from (select e.date,
                      e.num_errors::decimal*100/t.total_req as percentage
                      from errors e, total_requests t
                      where e.date = t.date) as error_percent
                      where percentage > 1;"""
                   )
    results = cursor.fetchall()

    # The for loop prints out the result as a numbered list.
    for row in results:
        print("\"{0}\" -- {1}% errors".format(row[0], round(row[1], 2)))

    print()


if __name__ == '__main__':
    """Calls all three functions."""

    first_question()
    second_question()
    third_question()

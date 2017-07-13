This application is called Logs-analysis. It queries data from news database to answer three questions. The program prints out the top three articles, top article authors with most views and days on which more than 1% requests resulted in error. news database has three tables. They are named log, articles and authors. Each table keeps track of different information. log table has information about what articles was accessed and when. it also keeps tracks of any errors that may occur. authors table has information such as authors name and bio. articles table has information about who wrote the article, title of the article and when it was written. Python 3.5 was used to develop this application. Psql is also required for this project. The program was written in vagrant VM.

The project has three files. They are called logs-analysis.py, newsdata.sql and Program_Output_Example.txt.

logs-analysis.py has three functions. one function for each question and each function contains one query. To answer the third question, two views were created. The code for those views can be found at the bottom of this document.

The newsdata.sql file was provided by the instructor. it contains all of the database tables and data. it is used to populate the database.

The Program_output_example.txt is a txt file that is a copy of what the program prints out.

Please follow these steps to run the program:

  1. how to create the news database and import schema and data into the database?
    - To start the program, you need to bring the virtual machine online with vagrant up and then log in by vagrant ssh. After logging in, please download the newsdata.sql file (link below) and populate the database using psql -d news -f newsdata.sql.

  2. where to get the newsdata.sql file with the database schema and data.
    - All of the data files can be found here:
      https://github.com/Mr-Sidhu/Logs-Analysis

  3. how to create the required views statements

    create view errors as
        SELECT date(log."time") AS date,
        count(log.status) AS num_errors
        FROM log
        WHERE log.status = '404 NOT FOUND'::text
        GROUP BY (date(log."time"))
        ORDER BY (count(log.status)) DESC;

    create view total_requests as
      SELECT date(log."time") AS date,
      count(log.status) AS total_req
      FROM log
      GROUP BY (date(log."time"))
      ORDER BY (count(log.status)) DESC;

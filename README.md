# Log Analysis

This a report tool used to generate statistics information based on a 
database server log from a newspaper. The database contains authors, 
articles and user's log viewing activity.

Those are the questions printed in the report in plain text format:

1 - What are the most popular three articles of all time?

2 - Who are the most popular article authors of all time?

3 - On which days did more than 1% of requests lead to errors?


## Requirements

In order to run this tool you will need:
- Vagrant and Oracle VirtualBox. Versions used and tested:
    - [Vagrant](https://www.vagrantup.com/downloads.html). Install the 
    version for your system;
    - [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
- Clone or download the project files. It includes the source codes, 
database files, and Vagrant configuration file. Get from [here](https://github.com/dtmarangoni/logs_analysis);
- Python 3 installed in Vagrant Linux VM(not tested with Python 2);
- Python 3 modules:
  - If not already, please install pip3;
  - psycopg2: `python sudo pip3 install psycopg2` and `sudo pip3 install 
  psycopg2-binary`;

## Instructions

1 - Get the Linux VM up and access it. Navigate to the project folder inside
 Vagrant shared folder.

2 - Unzip the database file - newsdata.sql, and use the command below to 
populate it with data:

`psql -d news -f newsdata.sql`

3 - Create the author_article_log database VIEW:

`psql -d news -f create_view.sql`

4 - Inside the project folder, run the command to execute the 
reporting tool;

`python3 log_analysis.py`

5 - The commands above must be run in the Linux VM environment and 
inside the project folder.


## Design

### Project contents:

#### 1- log_analysis.py
Python entry point of the program and LogAnalysis class. The class will 
contain the SQL queries and will process the queries results in a formatted 
plain text report.

It will make use of Database class inside database.py module in order to 
reach the database and execute the queries.

#### 2 - database.py
Python class responsible to access the PostgreSQL database. This class will 
ofter to log_analysis.py the database methods as well will treat the 
exceptions that might be raised from them.

##### Methods
- \_\_init\_\_(self, database): In order to use this class its necessary
  to create an instance and pass the database name as parameter;
- open_db_connection(self): Connect to the PSQL database defined by the 
  database parameter. After connected, the connection and cursor gets 
  prepared for use (internally);
- close_db_connection(self): Close the current PSQL database connection;
- execute_query(self, query): Execute the query in the PSQL database;
- get_results(self): Return all results from a previous executed query.
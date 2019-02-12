#!/usr/bin/env python3
#
"""The entry point for the python Log Analysis program.

It will connect to the database using the Database class and print out the
formatted plain text report.
"""

from database import Database


class LogAnalysis():
    """Entry class for Log Analysis program.

    It will connect to the database using the Database class and print out
    the formatted plain text report.
    """

    def __init__(self):
        """The constructor that will define the DB name and SQL queries."""
        self.DB_NAME = 'news'

        self.report = "\nLOG ANALYSIS REPORT\n\n" \
                      "1. What are the most popular three articles of all " \
                      "time?\n\n{}\n\n" \
                      "2. Who are the most popular article authors of all " \
                      "time?\n\n{}\n\n" \
                      "3. On which days did more than 1% of requests lead " \
                      "to errors?\n\n{}\n"

        self.QUERY_1 = """SELECT title, views FROM author_article_log
                        ORDER BY views DESC LIMIT 3"""

        self.QUERY_2 = """SELECT name, SUM(views) AS num FROM
                        author_article_log GROUP BY name ORDER BY num DESC"""

        self.QUERY_3 = """SELECT to_char(date, 'FMMonth DD, YYYY') AS date,
                        ROUND(error, 2) AS error_percent FROM(
                        SELECT time::date AS date,
                        100 * (COUNT(*) FILTER (WHERE status = '404 NOT FOUND')
                        / COUNT(*)::numeric) AS error
                        FROM log GROUP BY time::date) AS error_log
                        WHERE error > 1;"""

    def format_results(self, results=[], prefix="", suffix=""):
        """Format the query result table in a nicer way.

        If necessary provide the string prefix and/or suffix relative to
        results data.
        """
        formatted_table = ""
        for row in results:
            formatted_table += (prefix + "{0} - {1}" + suffix + '\n')\
                .format(row[0], row[1])
        return formatted_table

    def get_updated_report(self):
        """The main function of LogAnalysis class.

        It will connect to the database, execute all queries and print the
        final report.
        """
        # Create the database instance and connect to it
        db = Database(self.DB_NAME)
        db.open_db_connection()

        # Execute and fetch the first query and then get it formatted
        db.execute_query(self.QUERY_1)
        results_1 = db.get_results()
        results_1 = self.format_results(results_1, "", " views")

        # Execute and fetch the second query and then get it formatted
        db.execute_query(self.QUERY_2)
        results_2 = db.get_results()
        results_2 = self.format_results(results_2, "", " views")

        # Execute and fetch the third query and then get it formatted
        db.execute_query(self.QUERY_3)
        results_3 = db.get_results()
        results_3 = self.format_results(results_3, "", "% errors")

        # Close the database connection
        db.close_db_connection()

        # Return the formatted plain text report
        return self.report.format(results_1, results_2, results_3)


if __name__ == '__main__':
    """Entry point for the program."""
    print(LogAnalysis().get_updated_report())

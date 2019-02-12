"""A Database class to take care of a PSQL module database functions."""

import psycopg2


class Database():
    """The class responsible to manage DB connections and queries."""

    def __init__(self, database):
        """
        The constructor of Database object.

        It will initialize the connection and cursor objects as None.

        Args:
            database - the database name.
        Returns:
            No return.
        """
        self.database = database
        self.connection = None
        self.cursor = None

    def open_db_connection(self):
        """Connect to the PSQL database defined by the database parameter.

        After connected, the connection and cursor gets prepared for use.
        """
        try:
            self.connection = psycopg2.connect(database=self.database)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as error:
            print(error)
            if self.connection is not None:
                print("Closing DB connection.")
                self.connection.close()

    def close_db_connection(self):
        """Close the current PSQL database connection."""
        try:
            self.connection.close()
        except psycopg2.Error as error:
            print(error)

    def execute_query(self, query):
        """Execute the query in the PSQL database."""
        try:
            self.cursor.execute(query)
        except psycopg2.Error as error:
            print(error)

    def get_results(self):
        """Return the results from a previous executed query."""
        return self.cursor.fetchall()

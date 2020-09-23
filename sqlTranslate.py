
import mysql.connector
from mysql.connector import Error

class sqlTranslate(object):
    """
    Connects to MySQL and manipulates the database
    @date: 9/19/2020
    @author: Mehdi Hasanov
    """

    def __init__(self):
        """

        """
        self.connection = self.create_connection("localhost", "root", "*********", "sw_app")

    def create_connection(self, host_name, user_name, user_password, db_name):
        """
        Creates a connection to the SQL database
        @param host_name: 
        @param user_name: 
        @param user_password:
        @param db_name: 
        @return connection: connection needed in query use
        """
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection


    def execute_query(self, query):
        """
        Executes a SQL query passed in as a parameter
        @param query: query to be executed
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query):
        """
        Executes a SQL query passed in as a parameter
        Used for query that read data. Prints fields
        @param query: query to be executed
        @return result: data fetched by cursor
        """
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            print(column_names)
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def read_all(self, table : str):
        """
        Returns all the data in the specified table
        @param table: table name needed to fetch data
        """
        select_users = "SELECT * FROM %s" % (table)
        users = self.execute_read_query(select_users)

        for user in users:
            print(user)

    def create_table(self, name: str, fields: list, type: list,
                     fkey: list = list(), fkeyt:list = list(), fkeyf: list = list()):
        """
        Creates a table in the SQL database
        @param naem: name of table
        @param *argv: a list of field names AND respective types
        """

        query = """
        CREATE TABLE IF NOT EXISTS %s (
          id INT AUTO_INCREMENT""" % (name)
        for f, t in zip(fields, type):
            query = query + ", \n          " + "%s %s" % (f, t)
        query = query + """, \n          PRIMARY KEY (id)"""
        for f, t, ff in zip(fkey, fkeyt, fkeyf):
            query = query + "FOREIGN KEY(%s) REFERENCES %s(%s) ON DELETE SET NULL" % (f, t, ff)
        query = query + """
        ) ENGINE = InnoDB
        """
        self.execute_query(query)

    def drop_table(self, name: str):
        """
        Removes specified table from database
        @param name: name of thable to be removed
        """
        execute_query("DROP TABLE %s;" % (name))

    def drop_column(self, tname: str, cname: str):
        """
        Removes specified column/field from specified table
        @param tnaem: name of table
        @param cname: name of column to be removed
        """
        execute_query("ALTER TABLE %s DROP COLUMN %s;" % (tname, cname))

    def add_column(self, tname: str, cname: str, type: str):
        """
        Adds column/field to specified table
        @param tnaem: name of table
        @param cname: name of column to be added
        """
        execute_query("ALTER TABLE %s ADD %s %s;" % (tname, cname, type))

    def delete_record(self, tname: str, field: str, valaue: str):
        """
        Deletes recors
        @param tnaem: name of table
        @param field: field in which to search for value
        @param valaue: value at which record should be delted
        """
        delete_comment = "DELETE FROM %s WHERE %s = %s" % (tname, field, value)
        execute_query(delete_comment)

    def update_entrie(self, tname: str, fields: list, entriedata : list, local : str, localvalue : str):
        """
        
        """
        update_post_description = "UPDATE %s SET %s = %s" % (tname, fields, entriedata)
        update_post_description = update_post_description + " WHERE %s = %s" % (local, localvalue)
        execute_query(update_post_description)


        ######################UNFINISHED
    def isert_data(self, tname: str, fields: list, entriedata : list):
        values = ""
        for i in entriedata:
            if (values == ""):
                values = values + ", "
            values = values + i
        execute_query("INSERT INTO %s %s VALUES(%s);" % (tname, values))

"""
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
#######################################UNFINISHED

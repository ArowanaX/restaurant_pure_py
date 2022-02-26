import sqlite3
from sqlite3.dbapi2 import Cursor
import settings
from sqlite3 import Error


# ------------- creating connection ----------------------------

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# ----------------- creating table function ----------------------------------------------


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# -------------- creating table ------------------------------
def users():
    database = f"{settings.RESTORAN_DATA_PATH}/restoran.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text
                                    ); """

    sql_create_admin_table = """CREATE TABLE IF NOT EXISTS admins (
                                    id integer PRIMARY KEY,
                                    username text NOT NULL,
                                    password text
                                );"""

    sql_create_desert_table = """ CREATE TABLE IF NOT EXISTS deserts_menu (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        detail text,
                                        price integer
                                    ); """
    
    sql_create_drinks_table = """ CREATE TABLE IF NOT EXISTS drinks_menu (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        detail text,
                                        price integer
                                    ); """

    sql_create_main_table = """ CREATE TABLE IF NOT EXISTS main_menu (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        detail text,
                                        price integer
                                    ); """                                    

    sql_create_sefaresh_table = """ CREATE TABLE IF NOT EXISTS sefaresh (
                                    id integer PRIMARY KEY,
                                    sefaresh text,
                                    users_id integer NOT NULL,
                                    price integer,
                                    FOREIGN KEY (users_id) REFERENCES users (id)
                                ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)
        
        # create tasks table
        create_table(conn, sql_create_sefaresh_table)
        
        # create tasks table
        create_table(conn, sql_create_admin_table)

         # create tasks table
        create_table(conn, sql_create_desert_table)

         # create tasks table
        create_table(conn, sql_create_main_table)

         # create tasks table
        create_table(conn, sql_create_drinks_table)

        
    else:
        print("Error! cannot create the database connection.")


# ------------- create menu ----------------------------
def create_main(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO main_menu(name,detail,price)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_desert(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO deserts_menu(name,detail,price)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_drinks(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO drinks_menu(name,detail,price)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def main():
    database = f"{settings.RESTORAN_DATA_PATH}/restoran.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new main
        main = ('pitza', 'pitza hamechi', 45000);
        main_1 = create_main(conn, main)

        # create a new drinks
        drinks = ('fanta', 'noshabe kochik', 2000);
        drinks_1 = create_drinks(conn, drinks)

        # create a new desert
        desert = ('salad', 'salad darim ch saladi', 5000);
        desert_1 = create_desert(conn, desert)



# -------------- project --------------------------------

def get_main_menu():
    
    sqliteConnection = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from main_menu"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    return records




def get_drinks_menu():
    
    sqliteConnection = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from drinks_menu"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    return records


def get_deserts_menu():
    
    sqliteConnection = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from deserts_menu"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    return records
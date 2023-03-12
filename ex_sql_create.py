import sqlite3
from sqlite3 import Error


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


def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def add_route(conn, task):
    """
    Create a new routes into the routes table
    :param conn:
    :param route:
    :return: project id
    """
    sql = '''INSERT INTO routes(name, location, status,done_date)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def add_climber(conn, climber):
    """
    Create a new climber into the climbers table
    :param conn:
    :param route:
    :return: project id
    """
    sql = '''INSERT INTO climbers(name, lastname, age)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, climber)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":

    create_climbers_sql = """
    -- climbers table
    CREATE TABLE IF NOT EXISTS climbers (
        id integer PRIMARY KEY,
        name varchar(20) NOT NULL,
        lastname varchar(20) NOT NULL,
        age smallint
    );
    """

    create_routes_sql = """
    -- routes table
    CREATE TABLE IF NOT EXISTS routes (
        id integer PRIMARY KEY,
        climber_id integer ,
        name VARCHAR(250) NOT NULL,
        location TEXT NOT NULL,
        status bit,
        done_date smalldatetime,
        FOREIGN KEY (climber_id) REFERENCES climbers (id)
    );
    """

    db_file = "database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_climbers_sql)
        execute_sql(conn, create_routes_sql)
        climber = ("NNn", "Wwww", "18")
        add_climber(conn, climber)
        routes = [("Wwww", "OSP", "1", "2022-07-09"), ("Aaaa", "OSP",
                                                       "0", "2022-07-05"), ("Cccc", "Franken", "0", "2022-05-05")]
        for route in routes:
            pr_id = add_route(conn, route)

        conn.close()

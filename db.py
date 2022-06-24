import sqlite3
from sqlite3 import Error
import os


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
            
  
def delete_db(db_file):
    """ deletes the database """
    
    try:
        os.remove(db_file)    
    except Error as e:
        print(e)
        
def insert_session(conn, session_id,iscorrect):
    """
    insert a new session
    """
    if iscorrect:
        task=(session_id,1,0,1)
        sql = ''' INSERT INTO clicks(session_id,correct,incorrect,percentage)
              VALUES(?,?,?,?) '''
    else:
        task=(session_id,0,1,0)
        sql = ''' INSERT INTO clicks(session_id,correct,incorrect,percentage)
              VALUES(?,?,?,?) '''          
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    
def update_session(conn,session_id,iscorrect):
    """
    update session,
    """
    row=conn.execute("SELECT * FROM clicks WHERE session_id = ?",(session_id,)).fetchone()
    correct,incorrect=row[1],row[2]
    sql = ''' UPDATE clicks
              SET correct = ? ,
                  incorrect = ? ,
                  percentage = ?
              WHERE session_id = ?'''
    cur = conn.cursor()
    if iscorrect:
        correct+=1
        percentage=correct/(correct+incorrect)
        cur.execute(sql, (correct,incorrect,percentage,session_id))
    else:
        incorrect+=1
        percentage=correct/(correct+incorrect)
        cur.execute(sql, (correct,incorrect,percentage,session_id))
    conn.commit()    
    
def check_session(conn,session_id):
    """
    checks if session exists
    """
    if conn.execute("SELECT * FROM clicks WHERE session_id = ?",(session_id,)).fetchone():
        return True
    else:
        return False    
         
        
def main():
    database = r"clicks.db"

    sql_create_clicks_table = """ CREATE TABLE IF NOT EXISTS clicks (
                                        session_id text PRIMARY KEY,
                                        correct integer,
                                        incorrect integer,
                                        percentage real
                                        
                                    ); """

    

    # create a database connection
    conn = create_connection(database)

    # create table
    if conn is not None:
        # create clicks table
        create_table(conn, sql_create_clicks_table)
        
       
    else:
        print("Error! cannot create the database connection.")  

if __name__=="__main__":
    main()  
     

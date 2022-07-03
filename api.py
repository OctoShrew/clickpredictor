import json
from fastapi import FastAPI
import numpy as np
from typing import Dict, List
from db import create_connection,delete_db,check_session,update_session,insert_session
import sqlite3
app = FastAPI()
database = r"clicks.db"

# create a database connection
# conn = create_connection(database, connect_args={'check_same_thread': False})
conn = con = sqlite3.connect(database, check_same_thread = False)

# this should of course be a post method but doesn't work for browser testing
@app.get("/log_click", status_code=201)
def log_click(user_click: int, predicted_click: int, session_id: str) -> Dict:
    """
    user_click (int):  The click made by the user
    predicted_click (int): The prediction made by the system
    session_id (str): The session_id 

    logs a user's most recent click to store in the database and returns the user's percentage and             standard_deviation

    returns {percentage: float, standard_deviation: float}
    """
    if check_session(conn,session_id):
        update_session(conn,session_id,user_click == predicted_click)
    else:
        insert_session(conn, session_id,user_click == predicted_click)
        


@app.get("/get_data")
def get_data() -> List[float]:
    """
    returns a histogram of the performances achieved by users (based on the database) where each
    element contains the number of people having achieved a certain percentage
    """
    temp_list=conn.execute("SELECT * FROM clicks").fetchall()
    print("records-(session,correct,incorrect,percentage)",temp_list)
    percentages=[i[3] for i in temp_list]
    print("percentages",percentages)
    
    dist = np.random.normal(loc=65, scale=10, size=10000)
    dist = dist[dist < 100]
    dist = dist[dist > 0]
    bins = np.linspace(0, 100, 100)

    histogram = np.zeros_like(bins)
    bin_indexes = np.searchsorted(bins, dist)
    np.add.at(histogram, bin_indexes, 1)
    return list(histogram)
    
# log_click(1,1,"1")
# log_click(1,1,"1")
# log_click(2,1,"2")
# get_data()
    

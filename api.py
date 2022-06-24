import json
from fastapi import FastAPI
import numpy as np
from typing import Dict, List
app = FastAPI()


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
    if user_click == predicted_click:
        pass
        # database.put(session_id, correct=1, incorrect=0)
    else:
        # database.put(session_id, correct=0, incorrect=1)
    
    # if session_id already exists, increment correct/incorrect by the respective value
    # if session_id is new, create a new line with correct/incorrect starting at 0


@app.get("/get_data")
def get_data() -> List[float]:
    """
    returns a histogram of the performances achieved by users (based on the database) where each
    element contains the number of people having achieved a certain percentage
    """

    dist = np.random.normal(loc=65, scale=10, size=10000)
    dist = dist[dist < 100]
    dist = dist[dist > 0]
    bins = np.linspace(0, 100, 100)

    histogram = np.zeros_like(bins)
    bin_indexes = np.searchsorted(bins, dist)
    np.add.at(histogram, bin_indexes, 1)
    return list(histogram)

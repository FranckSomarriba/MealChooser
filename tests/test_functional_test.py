from flask import Flask
import json
from http import client
import mealchooser


def test_home_page():
    """
    GIVEN user request on choices
    WHEN the '/mealchooser' page is requested (GET)
    THEN check that the response is valid
    """    
       
    client = mealchooser.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
   


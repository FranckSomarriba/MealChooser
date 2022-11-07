from flask import Flask
from http import client
from mealchooser import app
from unittest import TestCase
from unittest.mock import patch
import pytest



def test_home_page():
    """
    GIVEN user request on choices
    WHEN the '/home' page is requested (GET)
    THEN check that the response is valid
    """    
       
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
   

def test_core_feature():
    """
    GIVEN user request on choices
    WHEN the '/mealchooser' page is requested (GET)
    THEN check that the response is valid
    """
    client = app.test_client()
    response = client.get("/mealchooser")

    assert response.status_code == 200

    
    
def test_login():
    """
    GIVEN user request on login
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """
    client = app.test_client()
    response = client.get("/login")

    assert response.status_code == 200
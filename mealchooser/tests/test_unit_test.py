from mealchooser import site_functions
import pytest

class TestRandomizer:
    def test_one(self):
        """
        GIVEN a POST request
        WHEN core feature is clicked
        THEN three names would be returned
        """      
        actual = len(site_functions.food())
        assert actual == 3       

    def test_two(self):
        """
        GIVEN a POST request for fast food
        WHEN core feature is clicked
        THEN three restaurants with food type "fast food" are returned
        """     
        for foods in site_functions.food():
            assert foods in site_functions.fastFoodDict.keys()




        

    
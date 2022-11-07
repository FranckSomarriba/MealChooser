import randomizer
import pytest

class TestRandomizer:
    def test_one(self):
        """
        GIVEN a POST request
        WHEN core feature is clicked
        THEN three names would be returned
        """      
        actual = len(randomizer.food())
        assert actual == 3       

    def test_two(self):
        """
        GIVEN a POST request for fast food
        WHEN core feature is clicked
        THEN three restaurants with food type "fast food" are returned
        """     
        for foods in randomizer.food():
            assert foods in randomizer.fastFoodDict.keys()




        

    
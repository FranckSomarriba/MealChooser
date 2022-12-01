from mealchooser import site_functions
import pytest
from mealchooser.models import User

class TestRandomizer:
    def test_case1(self):
        """
        If we give a POST request, it will return 3 names when feature is clicked.
    
        """      
        actual = len(site_functions.homecook())
        assert actual == 3       

    def test_case2(self):
        """
            If we give a POST request, it will return 3 names of homecook recipes with food type "recipe" when clicked.
        """     
        for foods in site_functions.homecook():
            assert foods in site_functions.recipeDict.keys()
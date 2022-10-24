import randomizer
import pytest

class TestRandomizer:
    def test_one(self):      # Unit test: Checks correct length of returned list
        actual = len(randomizer.food())
        assert actual == 3       

    def test_two(self):   # Unit test: Checks random foods are from the correct food type
        for foods in randomizer.food():
            assert foods in randomizer.fastFoodDict.keys()

class TestApp:
    def test_one(self):
        actual = 4
        assert actual == 3


        

    
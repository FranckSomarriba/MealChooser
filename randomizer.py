from random import sample
import pandas as pd

df = pd.read_csv('mealchooser.csv')       # Database is placed in a data frame
# Creation of a dictionary that has only fast food restaurants
fastFood = df[df["Type of Food"] == "Fast Food"].to_dict('split')
fastFoodDict = {}
for lists in fastFood["data"]:
    fastFoodDict[lists[0]] = lists[1:]

# Creation of a dictionary that has only recipes
recipe = df[df["Type of Food"] == "Recipe"].to_dict('split')
recipeDict = {}
for lists in recipe["data"]:
    recipeDict[lists[0]] = lists[1:]



def food_randomizer():
    """
    This function helps the user choose between fast food or recipe
    :return: Three keys
    """
    typeOfFood = input("What type of food do you want today?\nWrite 'F' for fast food, or 'R' for a home cook recipe: ")
    if typeOfFood.lower() == "f":
        mealChoices = sample(fastFoodDict.keys(), 3)
    else:
        mealChoices = sample(recipeDict.keys(), 3)

    return mealChoices

def food():
    mealChoices = sample(fastFoodDict.keys(), 3)
    return mealChoices


if __name__ == '__main__':

    print(food_randomizer())
from random import sample
import pandas as pd


df = pd.read_csv('mealchooser/mealchooser.csv')       # Database is placed in a data frame
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

def food():
    mealChoices = sample(list(fastFoodDict.keys()), 3)
    return mealChoices

def homecook():
    homecookChoices = sample(list(recipeDict.keys()),3)
    return homecookChoices

if __name__ == '__main__':
    print(food())

if __name__ == '__main__':
    print(homecook())

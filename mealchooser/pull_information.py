import pandas as pd
# Read CSV file into DataFrame
df = pd.read_csv('mealchooser.csv')
print(df)
# Load only selected columns
columns = ['Name','Type of Food']
df = pd.read_csv('mealchooser.csv', usecols =['Name','Type of Food'])
print(df)

# importing pandas package
import pandas as pd

# making data frame from csv file
df= pd.read_csv("mealchooser.csv")

# retrieving rows by loc method
row1 = df.iloc[[4, 5, 6, 7]]
print(row1)
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

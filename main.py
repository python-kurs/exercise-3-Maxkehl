# Exercise 3
from pathlib import Path
#import utils # no module named "utils"

# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
#%%
from pathlib import Path #importing 'pathlib' module
data_dir = Path("C:/Users/max-k/Documents/Git/exercise-3-Maxkehl/data")
# 2. Read the text file [2P]
# open(data_dir +"/cars.txt", "r")  # open with path  "data_dir" is not working: TypeError: unsupported operand type(s) for +: 'WindowsPath' and 'str'
import os
# os.path(data_dir+ "/cars.txt", "r") ) # open with os.path: invalid syntax
with open("C:/Users/max-k/Documents/Git/exercise-3-Maxkehl/data/cars.txt", "r") as file: # opening with whole path
    cars = file.readlines() #Umwandlung in Liste
print(cars)
 
# 3. Count the occurences of each item in the text file [2P]
#%%
#count = utils.count_type(cars) #utils kann nicht geladen werden
#count = cars.count(items)
#count = {n:cars(n) for n in cars}
#for n in cars:

#from collections import Counter
#[[x,.count(x)] for x in set(cars)]
 #   count.cars(n)
 

#print(count)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
solution = Path("data_dir") # Pfad für solutions festlegen
if not solution.exists():   # Überprüfe ob Ordner exsistiert
    Path("data_dir").mkdir(solution, parents = "true", exist_ok = "true") # wenn nicht, lege ihn an
#TypeError: an integer is required (got type WindowsPath) ????

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
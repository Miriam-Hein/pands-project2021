# analysis.py
# This program analysis the Fisher's Iris data set using python
# Author: Miriam Heinlein

# Numpy is a library for numerical computing. 
# matplotlib.pyplot is a library for data visualization

import pandas as pd #A nickname is assigned to all following libraries (pd, np, plt, sbn)
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sbn

# Load dataset (Fisher's Iris Data Set) using pandas
data = pd.read_csv('data/iris.csv') # pd.read_csv is used because imported pandas as pd (https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/) # CSV stands for Comma-Separated Values
# Load dataset using seaborn
#data = sbn.load_dataset('data/iris.csv') # https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
# To read the CSV file (https://www.guru99.com/python-csv.html)

print (data.head(10))
data.describe()


#with open ('data.txt', 'w') as file:
#     file.write(str(data))

#data["sepalLength"].describe() # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
#data["sepalWidth"].describe()
#data["petalLength"].describe()
#data["petalWidth"].describe()

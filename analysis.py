# analysis.py
# This program analysis the Fisher's Iris data set using python
# Author: Miriam Heinlein

# Pandas 
# Numpy is a library for numerical computing. 
# matplotlib.pyplot is a library for data visualization

import pandas as pd #A nickname is assigned to all following libraries (pd, np, plt, sbn) for better usability
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
#Set style for seaborn graphs #http://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

# Load dataset (Fisher's Iris Data Set) using pandas
iris = pd.read_csv('data/iris.csv') # pd.read_csv is used because imported pandas as pd (https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/, https://mer.vin/2019/08/seaborn-to-visualize-iris-data/) # CSV stands for Comma-Separated Values

 
with open ('summaryOfVariables.txt', 'w') as file:
     file.write(str(iris.describe())) # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
with open ('summaryOfVariables.txt', 'a') as file:
     file.write(str('\n'))
     file.write(str('\n'))
     file.write(str(iris["Species"].value_counts())) # https://www.kaggle.com/biphili/seaborn-matplotlib-iris-data-visualization-code-1
     file.write(str('\n'))
     file.write(str('\n'))
     file.write(str(iris.loc[iris["Species"] == "Iris-setosa"])) #usful for histogram

#Plotting histogram of each variable to png files

# Histogram for SepalLengthCm
sns.displot(iris, x="SepalLengthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalLength.png')   
plt.show ()

# Histogram for SepalWidthCm
sns.displot(iris, x="SepalWidthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalWidth.png')   
plt.show ()

# Histogram for PetalLengthCm
sns.displot(iris, x="PetalLengthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalLength.png')   
plt.show ()

# Histogram for PetalWidthCm
sns.displot(iris, x="PetalWidthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalWidth.png')   
plt.show ()

# removing Id column
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
# Histogram of all species for each variable using matplotlib.pyplot
f,a = plt.subplots(2,2)
a = a.ravel()
for idx,ax in enumerate(a):
    ax.hist(new_iris.iloc[:,idx], bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
    ax.set_title(new_iris.columns[idx])
plt.tight_layout()
#Save this plot as file
plt.savefig('PNG/Histogram_AllVariables.png')   
plt.show ()


#plt.figure(figsize=[10,10]) # https://www.datacamp.com/community/tutorials/histograms-matplotlib






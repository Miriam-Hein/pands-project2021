# analysis.py
# This program analysis the Fisher's Iris data set using python
# Author: Miriam Heinlein

# Pandas 
# Numpy is a library for numerical computing. 
# matplotlib.pyplot is a library for data visualization

import pandas as pd #A nickname is assigned to all following libraries (pd, np, plt, sbn) for better usability throughout the code
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import spellchecker
#Set style for seaborn graphs #http://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

# Load dataset (Fisher's Iris Data Set) using pandas from a file, uses comma as default delimiter
iris = pd.read_csv('data/iris.csv') # pd.read_csv is used because pandas library was imported, see pd.command (pd short for pandas as defined above). (https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/, https://mer.vin/2019/08/seaborn-to-visualize-iris-data/) # CSV stands for Comma-Separated Values

# removing Id column
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] # Creating a new iris dataset with only the columes required for the plot

# Creating a text file with Access mode write-only
with open ('summaryOfVariables.txt', 'w') as file: # Write-only mode: 'w' opens file for writing and creates a file or overwrites any existing files. File pointer is placed at the beginning of the file. 
     file.write(str('Summary statistics of variables for each species')) #https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
     file.write(str('\n'))
     file.write(str(new_iris.describe())) # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
# Appending the text file created with Access mode append
with open ('summaryOfVariables.txt', 'a') as file: # Append mode: 'a' opens file for appending. Starts writing at the end of the file. Creates new file if file is not existing. 
     file.write(str('\n')) # Creates new lines in the text file for better readability 
     file.write(str('\n'))
     file.write (str('Number of samples available for each species')) #https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
     file.write(str('\n'))
     file.write(str(iris["Species"].value_counts())) # https://www.kaggle.com/biphili/seaborn-matplotlib-iris-data-visualization-code-1
     file.write(str('\n')) # Creates new lines in the text file for better readability 
     file.write(str('\n'))
     file.write(str('Summary of correlations between variables')) 
     file.write(str('\n')) 
     file.write(str(new_iris.corr())) # Data Analysis and Visualization Using Python, Author: Dr. Ossama Embara, Page 281
  
   

#Plotting histogram of each variable to png files
# Histogram for SepalLengthCm
sns.displot(iris, x="SepalLengthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalLength.png')   
#plt.show ()

# Histogram for SepalWidthCm
sns.displot(iris, x="SepalWidthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalWidth.png')   
#plt.show ()

# Histogram for PetalLengthCm
sns.displot(iris, x="PetalLengthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalLength.png')   
#plt.show ()

# Histogram for PetalWidthCm
sns.displot(iris, x="PetalWidthCm", hue="Species", element="step") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalWidth.png')   
#plt.show ()

# removing Id column
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] # Creating a new iris dataset with only the columes required for the plot
# Histogram of all species for each variable using matplotlib.pyplot
f,a = plt.subplots(2,2) # defines subplot display structure
a = a.ravel() # a = array
for idx,ax in enumerate(a):
    ax.hist(new_iris.iloc[:,idx], bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85, facecolor='C0', edgecolor='C0') # https://www.pythonprogramming.in/plot-histogram-with-specific-color-edge-color-and-line-width.html
    ax.set_title(new_iris.columns[idx])
    ax.set_ylabel('Count') # https://stackoverflow.com/questions/53311685/difference-between-ax-set-xlabel-and-ax-xaxis-set-label-in-matplotlib-3-0-1
    ax.set_xlabel(new_iris.columns[idx])
plt.tight_layout() # it automatically adjusts the subplots parameters so that all subplots fit into the figure area. http://omz-software.com/pythonista/matplotlib/users/tight_layout_guide.html#:~:text=tight_layout%20automatically%20adjusts%20subplot%20params,%2C%20axis%20labels%2C%20and%20titles.

#Save this plot as file
plt.savefig('PNG/Histogram_AllVariables.png')   
#plt.show ()


#plt.figure(figsize=[10,10]) # https://www.datacamp.com/community/tutorials/histograms-matplotlib

#Plotting scatterplot of each pair of variables to png files
#Scatterplot of Sepal Width and Sepal Length features of the Fisher's Iris data
sepal = sns.scatterplot(data = iris, x="SepalLengthCm", y="SepalWidthCm", hue="Species") # https://seaborn.pydata.org/tutorial/relational.html
sepal.legend(loc=4) #Legend location assigned to bottom right corner inside plot window #https://stackoverflow.com/questions/27019079/move-seaborn-plot-legend-to-a-different-position

#Save this plot as file
plt.savefig('PNG/Scatterplot_Iris-Sepal.png')   
#plt.show ()

#Scatterplot of Petal Length and Petal Width features of the Fisher's Iris data
petal = sns.scatterplot(data=iris, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
petal.legend(loc=2) #Legend location assigned to top left corner

#Save this plot as file
plt.savefig('PNG/Scatterplot_Iris-Petal.png')   
#plt.show ()

#Pairplot
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]] #to remove Id column 
combination = sns.pairplot(data= new_iris, hue="Species", diag_kind="hist") # https://seaborn.pydata.org/generated/seaborn.pairplot.html

#Save this plot as file
plt.savefig('PNG/Pairplot_CombinationsSepalPetal.png')   
#plt.show ()
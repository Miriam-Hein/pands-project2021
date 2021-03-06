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
sns.histplot(iris, x="SepalLengthCm", hue="Species", element="step", kde=bool).set_title("Length of the sepal leaf in cm") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalLength.png')   
plt.show ()

# Histogram for SepalWidthCm
sns.histplot(iris, x="SepalWidthCm", hue="Species", element="step", kde=bool).set_title("Width of the sepal leaf in cm") # element="step" is used to resolve overlapping intervals. (https://seaborn.pydata.org/generated/seaborn.histplot.html)
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-SepalWidth.png')   
plt.show ()

# Histogram for PetalLengthCm
sns.histplot(iris, x="PetalLengthCm", hue="Species", element="step", kde=bool).set_title("Length of petal leaf in cm") # https://seaborn.pydata.org/tutorial/distributions.html
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalLength.png')   
plt.show ()

# Histogram for PetalWidthCm
sns.histplot(iris, x="PetalWidthCm", hue="Species", element="step", kde=bool).set_title("Width of petal leaf in cm") # https://seaborn.pydata.org/tutorial/distributions.html, https://stackoverflow.com/questions/42406233/how-to-add-title-to-seaborn-boxplot
#Save this plot as file
plt.savefig('PNG/Histogram_Iris-PetalWidth.png')   
plt.show ()

# removing Id column
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] # Creating a new iris dataset with only the columes required for the plot
# Histogram of all species for each variable using matplotlib.pyplot
fig,axes = plt.subplots(2,2) # defines subplot display structure (2 rows, 2 columns, figsize=(,)), figsize not defines
a = axes.ravel() # Convert nd array to 1D array (https://www.geeksforgeeks.org/differences-flatten-ravel-numpy/)
for idx,axes in enumerate(a): # couter of array
    axes.hist(new_iris.iloc[:,idx], bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85, facecolor='C0', edgecolor='C0') # https://www.pythonprogramming.in/plot-histogram-with-specific-color-edge-color-and-line-width.html
    axes.set_ylabel('Count') # https://stackoverflow.com/questions/53311685/difference-between-ax-set-xlabel-and-ax-xaxis-set-label-in-matplotlib-3-0-1
    axes.set_xlabel(new_iris.columns[idx]) # Using the index and counter enumerate to name each histograms x-axis
plt.tight_layout() # it automatically adjusts the subplots parameters so that all subplots fit into the figure area. http://omz-software.com/pythonista/matplotlib/users/tight_layout_guide.html#:~:text=tight_layout%20automatically%20adjusts%20subplot%20params,%2C%20axis%20labels%2C%20and%20titles.

#Save this plot as file
plt.savefig('PNG/Histogram_AllVariables.png')   
plt.show ()


#plt.figure(figsize=[10,10]) # https://www.datacamp.com/community/tutorials/histograms-matplotlib

#Plotting scatterplot of each pair of variables to png files
#Scatterplot of Sepal Width and Sepal Length features of the Fisher's Iris data
sepal = sns.scatterplot(data = iris, x="SepalLengthCm", y="SepalWidthCm", hue="Species") # https://seaborn.pydata.org/tutorial/relational.html
sepal.legend(loc=4) #Legend location assigned to bottom right corner inside plot window #https://stackoverflow.com/questions/27019079/move-seaborn-plot-legend-to-a-different-position
sepal.set_title("Length versus Width of the Sepal leaf in cm") 

#Save this plot as file
plt.savefig('PNG/Scatterplot_Iris-Sepal.png')   
plt.show ()

#Scatterplot of Petal Length and Petal Width features of the Fisher's Iris data
petal = sns.scatterplot(data=iris, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
petal.legend(loc=2) #Legend location assigned to top left corner
petal.set_title("Length versus Width of the Petal leaf in cm")

#Save this plot as file
plt.savefig('PNG/Scatterplot_Iris-Petal.png')   
plt.show ()

#Pairplot
new_iris = iris[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]] #to remove Id column 
sns.pairplot(data= new_iris, hue="Species", diag_kind="hist") # https://seaborn.pydata.org/generated/seaborn.pairplot.html

#Save this plot as file
plt.savefig('PNG/Pairplot_CombinationsSepalPetal.png')   
plt.show ()
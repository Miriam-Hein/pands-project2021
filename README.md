# Final project for the course Programming and Scripting 2021

This repository include the Final Project 2021 for the Module Programming and Scripting. 

This project contains the research of the ***Fisher's Iris data set*** which will be investigated in Python and a summary will be provided in this readme file. 
It will include background information about the data set used and will explain what investigating a data set entails and how Python can be used to do this. 

## Table of contents
* [Background](#Background)
    * [Summary of the Fisher's Iris data set](#Summary of the Fisher's Iris data set)
    * [Iris dataset file](#iris-dataset-file)
* [Dataset code and analysis](#dataset-code-and-analysis)
    * [Imported libraries and modules](#imported-libraries-and-modules)
        * [Libraries cheat sheets](#libraries-cheat-sheets)
    * [Dataset import](#dataset-import)
    * [Dataset summary](#datasetsummary)
        * [Summary of the values - describe()](#summary-of-the-values---describe())
        * [Samples of each type - info()](#samples-of-each-type---info())
* [Plots](#plots)
    * [Histograms](#histograms)
        * [Histogram code](#histogram-code)
    * [Scatterplots](#scatterplots)
        * [Scatterplot code](#scatterplot-code)
    * [Pairplot](#pairplot)
* [References](#references)
    * [Worthy mentions](#worthy-mentions)
    * [GitHub editing](#github-editing)
    * [Dataset analysis approach by others](#dataset-analysis-approach-by-others)





## Background

### Fisher's Iris data set

The *iris* is a genus of plants with around 260-300 different species with either yellow, blue or multi-colored petals, which is why this plant was named after the Greek goddess of the rainbow (iris). [1] 

![](PNG/Fig1_IrisSpecies.png) 

**Figure 1: Petals & Sepals for Iris setosa, Iris versicolor, and Iris virginica [1]**

Why this plant is described here is as follows:

Sir Ronald Aylmer Fisher was a British statistician and geneticist who published *“The Use of Multiple Measurements in Taxonomic Problems”* in the journal *“Annals of Eugenics”* in 1936. In his work, Fisher developed and evaluated a linear function for distinguishing iris species based on the morphology of their flowers, using the *Fisher’s Iris dataset*. This dataset is also called *Anderson’s Iris dataset* because Edgar Anderson’s collected the data mainly in Canada to quantify the morphological variation of iris flowers of three related species. [2,3]

The dataset contains values of 50 flowers of the three flower species *“Iris setosa”*, *“Iris versicolor”* and *“Iris virginica”*. For each flower, the following information was collected:
   - the length of the sepal leaf in cm ("sepalLength");
   - the width of the sepal leaf in cm (“sepalWidth”);
   - the length of the petal in cm (“petalLength”);
   - the width of the petal in cm (“petalwidth”); 
   - the species of flower ("class"). [2]

![](PNG/Fig2_IrisDataset.png) [2]

**Figure 2: Morphological Measures of Iris Flowers [1]**

### Python Analytics tool 


#### Libraries 

The following libraries were used in this project:    

```python
   import pandas as pd #A nickname is assigned to all following libraries (pd, np, plt, sbn) for better usability
   import numpy as np
   import matplotlib.pyplot as plt 
   import seaborn as sns 
```

***pandas***stands for "Python Data Analysis" and was created as an open source by Wes McKinney.
This project uses the library to take data directly from the csv file uploaded. This library creates a Python object with rows and columnes called dataframe (oftne refer to in code as df) which allows to work with a "table like" structure rather having to work with lists and/or directories using for loops/list comprehension. A "nickname"/ short for pandas has been created for better usability to access Pandas with "pd.command" instead of having to use "pandas.command". Numpy is usually used in combination with pandas. 
[4](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673)

***numPy***stands for "Numberical Python" and is the library that pandas, matplotlib and Scikit-learn are build on. It is not as default installed an therefore has to be added. This has been done at the start of this module via Anaconda. 
[5](https://towardsdatascience.com/a-quick-introduction-to-the-numpy-library-6f61b7dee4db)

***matplotlib***

***seaborn***

#### How to run the Python code and its purpose



## Analysis of the Fisher's Iris Data set

### Summary of Variables



### Histograms of Variables 

1. Length of the sepal leaf in cm ("SepalLengthCm")

![](PNG/Histogram_Iris-SepalLength.png) 

2. Width of sepal leaf in cm ("SepalWidthCm")

![](PNG/Histogram_Iris-SepalWidth.png) 

3. Length of petal leaf in cm ("PetalWidthCm") 

![](PNG/Histogram_Iris-PetalWidth.png) 

4. Width of petal leaf in cm ("PetalLengthCm")

![](PNG/Histogram_Iris-PetalWidth.png) 

5. Summary of all variables for Sepal Lenght/Width & Petal Length/Width, 

![](PNG/Histogram_AllVariables.png) 

### Scatterplots of pair of Variables 

## Interpretation of results

## Conclusion

## References

### References Summary of Fisher's Iris data set: 
[1] https://en.wikipedia.org/wiki/Iris_(plant) 
[2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 
[3] https://en.wikipedia.org/wiki/Iris_flower_data_set

### References Analysis of the Fisher's Iris Dataset



### PNG references: 
[1] Iris flower: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 
[2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 


### References & Source: 
Dataset: https://archive.ics.uci.edu/ml/datasets/Iris



## Tutorials used: 
[PNG added to readme] (https://www.youtube.com/watch?v=hHbWF1Bvgf4)
[Basic writing and formatting syntax in GitHub] https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
[Fenced code block added to readme] (https://docs.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks)



## Entries & Updates: 

11MAR21: Creation of git hub repository 
23MAR21: 
    - Uploaded dataset. Download dataset from https://archive.ics.uci.edu/ml/datasets/Iris.
      changed iris.data to iris.csv. Added Column titles to 
        1. sepal length (in cm)
        2. sepal width (in cm)
        3. petal length (in cm)
        4. petal width (in cm)
        5. class
      as per iris.names file section 7 Attributes. 
    - Started summary of the Fisher's Iris Dataset
19APR21: 
  - updated dataset from https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/ due to issues of unnamed columns. 
22APR21: 
  - created histograms of all variable using code in analysis.py and updated readme file

  
# =============================================================================
# the max values that can be stored in int64 is 
# 9,223,372,036,854,775,807
# with int32 :
# 2,147,483,647
# with int16:
# 32767
# 
# =============================================================================
# =============================================================================
# what is pandas 
# pandas is a python library used for working with datasets 
# 
# Functions:- 
# analyzing , cleaning , exploring and maniplating the data
# import the data from diffrent sources into python env 
# 
# pip install pandas 
# pip install modin"[all]"
# 
# mutithreading -> 12 core 
# only one core of my 12 cores are assigned to work with spyder 
# 
# =============================================================================
import pandas as pd 

#series
l1 = [1,2,3,4,5]
s = pd.Series([1,2,3,4,5])

s[2]

s = pd.Series(["p",2.2,2,2+0j,True,[1,2]])

#custom index
s1 = pd.Series(["p",2.2,2,2+0j,True,[1,2]],index=["p","y","t","h","o","n"])
s1[["p","y","t","h"]]

# =============================================================================
# #Numpy
# This is a package which allows us to work with arrays
# and the functions of numpy is to work with linear algebra , 
# fourier transformer and matrices
# 
# =============================================================================
import numpy as np 

data = np.array(l1)
data

data[2]

# creating a dataframe in python

data = {"name":["tom","jerry","spike","python","Java"]}

df = pd.DataFrame(data,index=["p","y","t","h","o"])

data1 = [("1/1/2019",13,6,"Rain"),
         ("1/2/2019",12,6,"Rain"),
         ("1/3/2019",2,np.NaN,"Fog"),
         ("1/3/2019",2,9,"Rain")]

df1 = pd.DataFrame(data1,columns=["day","temp","wspeed","event"])
#how to change column names after the dataframe is declared 

df1.columns = ["Date","Temperature","wind_speed","Day_be_like"]

#to print columns in python we are going to use columns function 

df1.columns

#transpose 
df2 = df1.T

df1.dtypes

df1.shape

df1.info()

df1.values

df1.head()

df1.head(1)

df1.tail()

df1.tail(1)

Outliers :- extream max or min values which are prest in your data

s = [6,5,100,4,8]

import statistics as st

st.mean(s)


Mean :- Average of all the number in a column 
Median :- Middle value or mid value in the column 
Mode :- Most occured Number/value in the column 
Variance :- Variance is a mesure of how foar a group of number are spread
SD   :- Measure of dispersion within a dataset is called as sd 
( Sigma or squareroot of Variance)


df1["Temperature"].mean()
df1["Temperature"].std()
df1["Temperature"].max()
df1["Temperature"].min()

df1.describe()

df1.describe(include=["object"])

df1.describe(include="all")


df = pd.read_csv("I:/Machine_Learning_and_Deep_Learning/Module 2 - Python for Data Science/2. Pandas/Pandas - 2/data/Iris.csv")
df.dtypes

df.shape

df.info()

df.values

df.head()

df.head(1)

df.tail()

df.tail(1)

pip install xlrd
pip install openpyxl

df.to_csv("test_csv.csv",index=False)
df.to_excel("test_csv.xlsx",index=False)

df11 = pd.read_excel("C:/Users/rajsa/test_csv.xlsx")

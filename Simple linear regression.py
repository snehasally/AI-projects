import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

df =pd.read_csv("C:/Users/rajsa/OneDrive/Desktop/Salary_Data.csv")

#outlire treatment 

s = df.describe()
plt.boxplot(df["Salary"])
plt.show()

#missing value
df.info()
df.isnull().sum()

x = df.iloc[:,0].values
y = df.iloc[:,1].values

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

x_train = x_train.reshape(-1,1)
y_train = y_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
y_test = y_test.reshape(-1,1)

regg = LinearRegression()
regg.fit(x_train,y_train)


pred = regg.predict(x_test)
pred1 = regg.predict(x_train)

plt.scatter(x_train,y_train,color="green")
plt.plot(x_train,pred1,color="red")
plt.show

s1 = pred1-y_train


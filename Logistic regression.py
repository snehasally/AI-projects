import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df = pd.read_csv("C:/Users/rajsa/OneDrive/Desktop/User_Data.csv")
df.columns
df = df.drop(["User ID"],axis=1)

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])

#outliers 
plt.boxplot(df["Age"])
plt.show()

plt.boxplot(df["EstimatedSalary"])
plt.show()

#missing values
df.info()

x = df.iloc[:,[0,1,2]].values
y = df.iloc[:,[3]].values

from sklearn.preprocessing import StandardScaler
st_x =StandardScaler()
x1 = st_x.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x1,y,test_size=0.2)


from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)


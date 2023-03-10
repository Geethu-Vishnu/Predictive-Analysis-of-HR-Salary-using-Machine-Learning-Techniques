# Importing all the libraries:

import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle

import warnings
warnings.filterwarnings('ignore')

data = pd.read_excel('salarydata.xls')

data.drop_duplicates(subset=None, keep='first', inplace=True)

# Replacing '?' in columns by 'other'
data['workclass'].replace(['?'],['other'],inplace=True)
data['occupation'].replace(['?'],['Other-services'],inplace = True)
data['native-country'].replace(['?'],['Other'],inplace=True)
data['marital-status'].replace(['Seperated'],['Divorced'],inplace=True)
data['marital-status'].replace(['Married-civ-spouse','Married-spouse-absent','Married-AF-spouse'],['Married','Married','Married'],inplace=True)

data.drop(['education-num','marital-status','relationship','race','capital-gain','capital-loss','native-country'],axis=1,inplace=True)
data = data.rename(columns={'hours-per-week':'hours_per_week'})

LabelEncoder = preprocessing.LabelEncoder()
col = ['workclass','education','occupation','sex','salary']
for col in data:
    data[col] = LabelEncoder.fit_transform(data[col])
    dt = data
# splitting the dataset into train and test data

x = dt.drop(['salary'],axis=1)
y = dt['salary']


# Logistic Regression Model

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42 , test_size=0.2)
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train,y_train)

pickle.dump(lr, open('model.pkl','wb'))


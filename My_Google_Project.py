# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:08:14 2022

@author: dell
"""


"""
Created on Sun Apr 21 10:16:34 2022

@author: Aman.Verma
"""


##########################################################################################
#------------------------------------Pandas In Python-------------------------------------#
##########################################################################################

import pandas as pd
import numpy as np
import os

#Setting the working directory

os.chdir(R'C:\Users\dell\Documents\PYTHON_SCRIPTS\PANDAS')

path_data = os.getcwd()

#Master_Path
path_data= R'C:\Users\dell\Documents\PYTHON_SCRIPTS\PANDAS'
print(path_data)


#Branch_Path
input_path = os.path.join(path_data,"input")#Sub Folder1 
output_path = os.path.join(path_data,"output")#Sub Folder 2


#------------------------------------------CSV---------------------------------------#

employee_df = pd.read_csv(os.path.join(input_path,"employees.csv"))
GoogleData = pd.read_csv("Googleplaystore_1.csv")

##########################################################################################
#3.Viewing Data
##########################################################################################

#Head of Data
GoogleData.head()

First_100=GoogleData.head(100)

#Tail of Data
GoogleData.tail()
Last_10=GoogleData.tail(10)


#Viewing the Columns of Data
GoogleData.columns

#Checking the Structure of Data
GoogleData.dtypes


# Print the info of Data
print(GoogleData.info())


#Summary of the Data
Des=GoogleData.describe()


#Including all the Data Levels
Des_all=GoogleData.describe(include='all')


#GoogleData_1 = GoogleData[(GoogleData.Category == "FAMILY")]

# Print the shape of Data
print(GoogleData.shape)



##########################################################################################
#4.Changing the type of data
##########################################################################################

#Converting a coloumn to a particular Data Type
pd.to_numeric(GoogleData.Rating)

#Multiple Columns
GoogleData_1=GoogleData.copy()
GoogleData_1.dtypes

#Univariate changes
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(str)
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(float)

#Multivariate changes

GoogleData_1[["Rating","Reviews"]] = GoogleData_1[["Rating","Reviews"]].apply(str)#Making same changes across columns
GoogleData_1 = GoogleData_1.astype({"Rating":'str',"Reviews":'float'})#Making different changes across columns
GoogleData_1.dtypes


##########################################################################################
#5.Selecting the Data
##########################################################################################


#Selecting only one Column 
GoogleData1= GoogleData['App']
GoogleData1= GoogleData[['App','Rating','Reviews','Category']]
GoogleData1= GoogleData.App

#Selecting only Multiple Columns

col_list = ['App','Category','Rating','Reviews']
GoogleData2= GoogleData[col_list]

#Based on Labels
GoogleData2= GoogleData.loc[:,'App']# All Rows

GoogleDat2= GoogleData.loc[200:300,['App','Size','Reviews']]
GoogleDat2.shape

#Based on Index
GoogleData2= GoogleData.iloc[:,[2,3,10]]

#Selecting Multiple Rows
GoogleData2= GoogleData.iloc[0:3,:]
GoogleData2_iloc= GoogleData.iloc[0:3,3:10]
GoogleData2_loc = GoogleData.loc[0:3,['App','Size']]

##########################################################################################
#6. Filtering the Data
##########################################################################################

GoogleData3 = GoogleData[GoogleData.Rating == 3].reset_index(drop=True)

GoogleData3 = GoogleData[GoogleData.Rating == 3]


GoogleData3 = GoogleData[GoogleData['Rating'] > 3]


#AND
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )].reset_index(drop=True)

#OR
GoogleData5 = GoogleData[(GoogleData.Rating > 3) | (GoogleData.Reviews > 10000 ) ]


#AND & OR
GoogleData5 = GoogleData[((GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )) | (GoogleData.Category == "ART_AND_DESIGN")]


GoogleData6 = GoogleData[GoogleData['Category'].isin(["ART_AND_DESIGN","HEALTH_AND_FITNESS"])]

#NOT
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & ~(GoogleData.Reviews > 10000 )]

#MULITPLE NOT
GoogleData4 = GoogleData[~(GoogleData.Rating ==3) & ~(GoogleData.Reviews > 10000 )]
GoogleData4.to_csv(os.path.join(output_path,"Processed_Google_Data.csv"),index=False)

##########################################################################################
#7. Working with Missing Data
##########################################################################################

#pandas primarily uses the value np.nan to represent missing data

#Finding the columns with Missing Values
Miss = GoogleData.isnull().sum()
Miss_df = pd.DataFrame({'Missing_Value_Count':GoogleData.isnull().sum()}).reset_index()


#Total Sum of Missing Values
GoogleData.isnull().sum().sum()

#Imputing Missing values withe particular value
GoogleData7=GoogleData.fillna(value=0)
Miss = print(GoogleData7.isnull().sum())

#Working with particular columns
GoogleData7=GoogleData.copy()
GoogleData7['index']=GoogleData7.index
GoogleData7['Rating'] = GoogleData7['Rating'].fillna((GoogleData7['Rating'].mean()))

#Filtering based on odd rows
GoogleData7_odd = GoogleData7[::3]#N-1
GoogleData7_odd = GoogleData7[::2]

#Filterinf based on even rows
GoogleData7_even = GoogleData7[1::2]

#Append two data frames in Pandas
GoogleData8=GoogleData7.head(10).append(GoogleData7.tail(10)).reset_index(drop=True)
GoogleData8=GoogleData7.head(10).append([GoogleData7.tail(10),GoogleData7.tail(2)])
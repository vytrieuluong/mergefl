import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import LabelEncoder
import openpyxl


dataset = pd.read_excel("trainClinData.xls")
dataset = dataset.replace(r'^\s*$', np.nan, regex=True)

# Creating an instance of label Encoder.
le = LabelEncoder()
# Using .fit_transform function to fit label encoder and return encoded label
label = le.fit_transform(dataset["Prognosis"])
dataset["Prognosis"] = label
del dataset["Fibrinogen"]
del dataset["PCT"]
del dataset["D_dimer"]
del dataset["SaO2"]
del dataset["Obesity"]


testdataset = pd.read_excel("testClinData.xls")
testdataset = testdataset.replace(r'^\s*$', np.nan, regex=True)

le = LabelEncoder()

label = le.fit_transform(testdataset["Prognosis"])
testdataset["Prognosis"] = label
del testdataset["Fibrinogen"]
del testdataset["PCT"]
del testdataset["D_dimer"]
del testdataset["SaO2"]
del testdataset["Obesity"]

dataset.to_excel('trainClinData.xls', sheet_name='trainset')
testdataset.to_excel('testClinData.xls',sheet_name='testset')
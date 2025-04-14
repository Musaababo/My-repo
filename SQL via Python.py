import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv("diabetes.csv")
#task 3
print(len(diabetes_data.columns))
# another way, print(diabetes_data.shape)

#task4
print(len(diabetes_data))

#task 5
print(diabetes_data.isnull().sum())
#print(diabetes_data.info())
#6
print(diabetes_data.describe())

#9
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

#10
print(diabetes_data.isnull().sum())

#11
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#13
print(diabetes_data.dtypes)

#14
print(diabetes_data.Outcome.unique())

#15
diabetes_data["Outcome"] = diabetes_data ["Outcome"].replace("O","0")

#16 Trying to replace the value of 0 ro NaN
#diabetes_data ["Outcome"] = diabetes_data ["Outcome"].replace("0", "NaN")



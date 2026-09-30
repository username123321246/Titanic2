import pandas as pd
import random

asd = pd.read_csv("LESSONS\\titanic.csv")

#Get the particular columnm out of a condition
sdf = asd.loc[asd["Age"] > 18, "Age"]
print(sdf.head())
print()

#Slicing
print(asd.iloc[1:6, 5])
print()

#Update the value with the help of slicing
asd.iloc[2:8, 6 ] = 123456789
print(asd["Parents/Children Aboard"])

#Save the data
asd.to_csv("Titanic2.csv")

#Creating a new column in the data set
Hobbies = ["Football", "Tennis", "Singing", "Basketball", "Drawing", "Baseball", "Dancing"]
asd["Hobby"] = [random.choice(Hobbies) for i in range(887)]
print(asd.head())

#Renaming the columns
renamed = asd.rename(columns = {"Sex":"Gender"})
print(renamed.head())



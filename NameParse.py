#   1 - Create a data frame of 10 random names (first, last, and title)
#   2 - Define a function to parse the first, last, and title
#   3 - Define new columns for data frame for first, last, and title
#   4 - Use the functions in a loop to parse the data into the columns


#Import modules
from nameparser import HumanName
import pandas as pd
import numpy as np
import re


#Question 1

#Create a data frame
data = {'Names' : ['Ms. Margo Robbie', 'Dr. James Brown', 'Ms. Sonia Smith', 'Mr. Austin Powers', 'Mrs. Juliana Chambers', 'Ms. Zoe Ziti', 'Mr. Jacob Fisher', 'Mrs. Julia Roberts', 'Mr. John Parish', 'Dr. Samantha Jones']}
df = pd.DataFrame(data)

print(df)


#Question 2

#Define a function to parse
def parse():
    df['Title'] = df['Names'].apply(lambda x: HumanName(x).title)
    df['First Name'] = df['Names'].apply(lambda x: HumanName(x).first)
    df['Last Name'] = df['Names'].apply(lambda x: HumanName(x).last)

#What is lambda?
#lambda function is used when we need a function for a short period of time.
#It can take any number of arguments but contain one expression
#It is used to return function objects


#Question 3

#Define new columns for the data frame
df['First Name'] = np.nan
df['Last Name'] = np.nan
df['Title'] = np.nan

print(df)


#Question 4

#Use the function to loop
for name in df.iterrows():
    parse()

print(df)

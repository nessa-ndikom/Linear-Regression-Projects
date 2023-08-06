import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns

# the sep parameter is used here bc the thing used to separate values in the csv file (the delimiter) is a semicolon (;)...
# ...instead of a comma (,). Using sep tells the computer that a (;) was used instead of a (,)
df = pd.read_csv(r'student\student-mat.csv', sep=";")

# the df.describe() method gives a statistical summary of the dataset, with mean, std (standard deviation), etc.
# print(df.describe())

# df.info() method gives you info about the types of the valuesin the dataset
print(df.info())

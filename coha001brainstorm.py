import pandas as pd
import numpy as np
#for the current test cases the first column is row 1 and row 2
class NNClassflier():
    def __init__(self,file_name):
        self.file_name = file_name
        self.df = pd.DataFrame()
file_name = 'small-test-dataset.txt'
file = open(file_name, "r")
file_content = file.readlines()
# ideal state
df = []
x = file_content[0].split()
z = [float(item) for item in x]
print(x)
print(z)
for row in file_content:
    string_row = row.split()
    df_row = [float(item) for item in string_row]
    df.append(df_row)

array = np.array(df)
print(array)
array_Transpose = array.T
print(array_Transpose)
for i in range(1,len(array_Transpose)):
    mean = np.mean(array_Transpose[i])
    std_dev = np.std(array_Transpose[i])
    array_Transpose[i] = (array_Transpose[i] - mean)/std_dev
final_array = array_Transpose.T
print(final_array)
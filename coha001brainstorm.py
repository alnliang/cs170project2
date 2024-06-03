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
# for each mean you can store in an array and just print array and std
for i in range(1,len(array_Transpose)):
    mean = np.mean(array_Transpose[i])
    std_dev = np.std(array_Transpose[i])
    array_Transpose[i] = (array_Transpose[i] - mean)/std_dev
final_array = array_Transpose.T


import matplotlib.pyplot as plt
classes = final_array[:,0]

class_labels = np.unique(classes)

class_counter = np.zeros(len(np.unique(classes)))
#data visualiztion for each class
print(len(class_counter))
for label in class_labels:
    print(label)
    print(int(label))
for i in range(len(classes)):
    for label in class_labels:
        if classes[i] == label:
            class_counter[int(label)-1] += 1
plt.figure(figsize=(8, 6))
plt.bar(class_labels, class_counter, color='skyblue')
plt.title('Instance Count per Class')
plt.xlabel('Class Labels')
plt.ylabel('Instance Count')
plt.grid(axis='y')
plt.show()
import matplotlib.pyplot as plt

# Assuming your data is stored in a variable called 'data'
# Extract class labels and features
class_labels = final_array[:, 0]
features = final_array[:, 1:]

# Plot each data point with color based on its class label
for i in range(len(class_labels)):
    if class_labels[i] == 1:
        plt.scatter(features[i, 0], features[i, 1], color='red')
    elif class_labels[i] == 2:
        plt.scatter(features[i, 0], features[i, 1], color='blue')
    else:
        plt.scatter(features[i, 0], features[i, 1], color='green')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Data colored by class')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#for the current test cases the first column is row 1 and row 2
class NNClassflier():
    def __init__(self,file_name):
        self.file_name = file_name
        self.df = pd.DataFrame()
file_name = 'large-test-dataset.txt'
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


class_labels = final_array[:, 0]
features = final_array[:, 1:]


for i in range(len(class_labels)):
    if class_labels[i] == 1:
        plt.scatter(features[i, 22], features[i, 35], color='red')
    elif class_labels[i] == 2:
        plt.scatter(features[i, 22], features[i, 35], color='blue')
    else:
        plt.scatter(features[i, 0], features[i, 1], color='green')

plt.xlabel('Feature 23')
plt.ylabel('Feature 36')
plt.title('Data colored by class')
plt.show()
for i in range(len(class_labels)):
    if class_labels[i] == 1:
        plt.scatter(features[i, 15], features[i, 28], color='red')
    elif class_labels[i] == 2:
        plt.scatter(features[i, 15], features[i, 28], color='blue')
    else:
        plt.scatter(features[i, 15], features[i, 28], color='green')

plt.xlabel('Feature 16')
plt.ylabel('Feature 29')
plt.title('Data colored by class')
plt.show()
for i in range(len(class_labels)):
    if class_labels[i] == 1:
        plt.scatter(features[i, 27], features[i, 32], color='red')
    elif class_labels[i] == 2:
        plt.scatter(features[i, 27], features[i, 32], color='blue')
    else:
        plt.scatter(features[i, 27], features[i, 32], color='green')

plt.xlabel('Feature 28')
plt.ylabel('Feature 33')
plt.title('Data colored by class')
corr_matrix = np.corrcoef(features, rowvar=False)
plt.show()
# #use that only for large data set
# #plt.figure(figsize=(22, 20))
# sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='viridis', linewidths=.5, linecolor='white', cbar=True, cbar_kws={'shrink': 0.8})
# plt.show()
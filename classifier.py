from coordinate import Coordinate 
import numpy as np
import pandas as pd
import sys
class Classifier:
    def __init__(self):
        self = self
        self.instances = []
        self.df = []
        self.true_labels = []
    def train(self, file_name):
        output = open(file_name, 'r')
        lines = output.readlines()
        count = 0
        for line in lines:
            count += 1
            individual = line.split()
            label = float(individual[0])
            individual.pop(0)
            #print(f"Line {count}: {label}: {individual}")
            temp = []
            for number in individual:
                temp.append(float(number))
            npTemp = np.array(temp)
            coordinate = Coordinate(label, npTemp)
            self.instances.append(coordinate)
            #print(f"{label}")
        return
    def test(self, index, features):
        #find closest point
        a = []
        b = []
        temp = self.df.copy()
        #print(f"{temp}")
        temp = np.delete(temp, index, 0)
        #print(f"{temp.size}")
        #print(f"{temp}")
        min = sys.maxsize
        minIndex = 0
        count = 0
        for feature in features:
            np.append(a, self.df[index][feature])
            a.append(self.df[index][feature])
        for point in temp:
            for f in features:
                np.append(b, point[f])
                b.append(point[f])
            res = euclideanDistance(a, b)
            print(f"Coord {count + 1} \n\t Label: {point[0]} \n\t Distance: {res} \n\t Coords: {b} \n")
            if(res < min):
                min = res
                minIndex = count
            count += 1
            b = []
        print(f"Final Results: \n\t Label: {temp[minIndex][0]} \n\t Coord: {minIndex} \n\t Distance: {min}")
        print(f"Dataset Length: {len(self.df)}, Temp Length: {len(temp)}")
        return temp[minIndex][0]
    def printCoords(self):
        for instance in self.df:
            print(f"{instance.label}: {instance.coords}")
    #todo for get_df make it a dataframe instead getting features will be easier later on.
    #file_name = 'small-test-dataset.txt'
    def get_df(self,file_name):
        #part 1 extracting 
        file = open(file_name, "r")
        file_content = file.readlines()
        temp_df = []
        for row in file_content:
            string_row = row.split()
            df_row = [float(item) for item in string_row]
            temp_df.append(df_row)
        array = np.array(temp_df)
        # part 2 normalizing it first have to transpose it and then normalize
        # during this part we can also store the true values
        array_Transpose = array.T
        self.true_labels = array_Transpose[0]
        for i in range(1,len(array_Transpose)):
            mean = np.mean(array_Transpose[i])
            std_dev = np.std(array_Transpose[i])
            array_Transpose[i] = (array_Transpose[i] - mean)/std_dev
        self.df = array_Transpose.T
        #part 3 make into a df to do
    def accuracy(self, test_labels):
        correct_count = 0
        for i in range(1,len(test_labels)):
            if test_labels[i] == self.true_labels[i]:
                correct_count += 1
        return correct_count/len(self.true_labels)


def euclideanDistance(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    dist = np.linalg.norm(a - b)
    return dist


classifier = Classifier()
classifier.get_df("small-test-dataset.txt")

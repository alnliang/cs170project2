from coordinate import Coordinate 
import numpy as np
import pandas as pd
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
    def test(self, instance, num_features):
        #find closest point
        
        return
    def printCoords(self):
        for instance in self.instances:
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


classifier = Classifier()
classifier.get_df("small-test-dataset.txt")
print(classifier.df)
#classifier.printCoords()
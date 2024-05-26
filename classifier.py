from coordinate import Coordinate 
import numpy as np
import os
class Classifier:
    def __init__(self):
        self = self
        self.instances = []
    def train(self, file):
        output = open(file, 'r')
        lines = output.readlines();
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
        count = 0
        for instance in self.instances:
            count += 1
            if instance.coords.size != 10: #sanity check make sure no errors during parsing
                print(f"Something is wrong at line {count}")
                break
            print(f"Line {count}: Label: {instance.label}: Length: {instance.coords.size} Coords: {instance.coords}")

classifier = Classifier()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'small-test-dataset.txt')
#print(f"{filename}")
classifier.train(filename)
classifier.printCoords()
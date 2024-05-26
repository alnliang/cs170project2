from coordinate import Coordinate 
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
            coordinate = Coordinate(label, temp)
            self.instances.append(coordinate)
            #print(f"{label}")
        return
    def test(self, instance):
        #find closest point
        return
    def printCoords(self):
        for instance in self.instances:
            print(f"{instance.label}: {instance.coords}")

classifier = Classifier()
classifier.train("/Users/redditravager/Documents/cs170project2/small-test-dataset.txt")
classifier.printCoords()
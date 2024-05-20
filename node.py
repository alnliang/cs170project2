import random
class Node:
    def __init__(self,subset):
        self.subset = subset
        self.accuracy = 0
    #change get accuracy later, psuedo code
    def get_accuracy(self):
        self.accuracy =round(random.random()*100,3)

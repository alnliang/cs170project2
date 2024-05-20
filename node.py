import random
import copy
class Node:
    def __init__(self,features):
        self.subset = features
        self.accuracy = 0
        self.next = []
    #change get accuracy later, psuedo code
    def get_accuracy(self):
        self.accuracy =round(random.random()*100,3)
    #to get additional_feature
    def additional_feature(self, num_features):
        all_feature = [i for i in range(1, num_features + 1)]
        subset = self.subset
        additonal_feature = [i for i in all_feature if i not in subset]
        return additonal_feature

    #features are the features in the current node, while num_features are the totat number of features aviable
    #for instance a current state can just be 1 but has a total number of features of 4
    def get_next_states(self, num_feature):
        additonal_feature = self.additional_feature(num_feature)
        for feature in additonal_feature:
            new_subset = copy.deepcopy(self.subset)
            new_subset.append(feature)
            self.next.append(new_subset)


n1 = Node([])
print(n1.additional_feature(4))
print(n1.get_next_states(4))
n2 = Node([1])
print(n2.additional_feature(4))
n3 = Node([1,2])
n4 = Node([1,2,3])
n5 = Node([1,2,3,4])
print(len(n1.subset))
        
list1 = [1, 2, 3, 4]
list2 = [1, 2]
unique_to_list1 = [i for i in list1 if i not in list2]
print(unique_to_list1)

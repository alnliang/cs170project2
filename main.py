from node import Node 
import random
def forward(feature):
    trace = []
    explored = []
    curr_node = Node({})
    curr_node.get_accuracy()
    trace.append(curr_node)
    reached_end_state =False
    while len(curr_node.subset) != feature:
        continue

    return trace
def backward(num_features):
    trace = []
    explored = []
    features = [i for i in range(1, num_features + 1)]
    curr_node = Node(features)
    max = curr_node.get_accuracy()
    maxPrev = curr_node.get_accuracy()
    trace.append(curr_node)
    print(f"Using all features and random evaluation, I get an accuracy of {max}%\n")
    while len(curr_node.subset) != 0:
        prev = curr_node.get_prev_states(num_features)
        explored.append(curr_node.subset)
        for node in prev:
            if node.subset in explored:
                continue
            trace.append(node)
            accuracy = node.get_accuracy()
            print(f"Using feature(s) {node.subset} accuracy is {accuracy}%\n")
            if(accuracy > max):
                max = accuracy
                curr_node = node
        if(max == maxPrev):
            print("Warning, accuracy has decreased!\n")
            break
        maxPrev = max
        print(f"Feature set {curr_node.subset} was the best with an accuracy of {max}%")     
    return
def special():
    return
print("Welcome to Charles and Alan's Feature Selection Algorithm")
features = int(input("Please enter total number of features"))
algo_option = int(input("Type the number on the algorithm you want to run: 1 for foward, 2 for backward, 3 for special"))
if algo_option == 1:
    trace = forward()
    print(f"use no features and \"random\" evaluation, I get an accuracy of {trace[0].accuracy} %")
if algo_option == 2:
    # trace = backward()
    # print(f"use all features and \"random\" evaluation, I get an accuracy of {trace[0].accuracy} %")
    backward(features)
print("Beginning Search")
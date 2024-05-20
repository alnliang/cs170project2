from node import Node 
import random
def forward(feature):
    trace = []
    explored = []
    intitial_node = Node({})
    intitial_node.get_accuracy()
    trace.append(intitial_node)
    reached_end_state =False
    while reached_end_state == False:
        if len(explored[0] == feature):
            reached_end_state = False
            break
        
    return trace
def backward():
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
    trace = backward()
    print(f"use all features and \"random\" evaluation, I get an accuracy of {trace[0].accuracy} %")
print("Beginning Search")
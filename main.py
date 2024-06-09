from node import Node 
import random
def forward(feature):
    curr_node = Node([])
    best_accuracy = curr_node.get_accuracy()
    print(f"use no features and 1-nearest neighbor evaluation, I get an accuracy of {curr_node.accuracy} %")
    print("Beginning Search")
    while len(curr_node.subset) != feature:
        curr_node.get_next_states(feature)
        for state in curr_node.next:
            state.get_accuracy()
            print(f"Using features ({state.subset}) accuracy is {state.accuracy} %")
        prev_node = curr_node
        curr_node = curr_node.get_highest_child_accuracy()
        print(f"Feature set was best {curr_node.subset}, accuracy is  {curr_node.accuracy}")
        if curr_node.accuracy > best_accuracy:
            best_accuracy = curr_node.accuracy
        else:
            print("(Warning Accuracy Decreased)")
            print(f"Finished Search !! The best feature subset is {prev_node.subset}, accuracy is  {prev_node.accuracy}")
            break        
    return 

def backward(num_features):
    trace = []
    explored = []
    features = [i for i in range(1, num_features + 1)] #starts with full suite of features, if i = 4 then [1, 2, 3, 4]
    curr_node = Node(features) 
    max = curr_node.get_accuracy()
    maxPrev = curr_node #previous node with the highest accuracy
    trace.append(curr_node)
    print(f"Using all features and 1-Nearest Neighbor evaluation, I get an accuracy of {max}%\n") #print accuracy of node with all features
    while len(curr_node.subset) != 0:
        prev = curr_node.get_prev_states(num_features) #get_prev_states(num_features) gets all possible nodes with num_features - 1 features. 
        explored.append(curr_node.subset)
        for node in prev:
            if node.subset in explored: #so no repeating nodes explored, just a failsafe, unlikely to happen
                continue
            trace.append(node)
            accuracy = node.get_accuracy() #runs random evaluation function, and saves the result
            print(f"Using feature(s) {node.subset} accuracy is {accuracy}%\n")
            if(accuracy > max): #setting new max if found
                max = accuracy
                curr_node = node
        if(curr_node == maxPrev): #if the maximum node has not changed, then the maximum is assumed to have been found already
            print("Warning, accuracy has decreased!\n")
            break
        maxPrev = curr_node
        print(f"Feature set {curr_node.subset} was the best with an accuracy of {max}%\n")
    print(f"Overall, Feature set {curr_node.subset} was the best with an accuracy of {max}%")        
def forward_backward(feature_count):
    print("Beginning Combined Search")

    forward_curr_node = Node([])
    forward_best_accuracy = forward_curr_node.get_accuracy()
    print(f"Use no features and \"random\" evaluation, I get an accuracy of {forward_curr_node.accuracy:.2f} %")

    backward_curr_node = Node([i for i in range(1, feature_count + 1)])
    backward_best_accuracy = backward_curr_node.get_accuracy()
    print(f"Using all features and \"random\" evaluation, I get an accuracy of {backward_curr_node.accuracy:.2f} %")

    while True:
        forward_curr_node.get_next_states(feature_count)
        for state in forward_curr_node.next:
            state.get_accuracy()
            print(f"Using features ({state.subset}) accuracy is {state.accuracy:.2f} %")

        forward_prev_node = forward_curr_node
        forward_curr_node = forward_curr_node.get_highest_child_accuracy()
        print(f"Forward feature set was best {forward_curr_node.subset}, accuracy is {forward_curr_node.accuracy:.2f} %")
        if forward_curr_node.accuracy > forward_best_accuracy:
            forward_best_accuracy = forward_curr_node.accuracy
        else:
            print("(Warning Accuracy Decreased)")
            print(f"Finished Forward Search! The best feature subset is {forward_prev_node.subset}, accuracy is {forward_prev_node.accuracy:.2f} %")
            break

        backward_prev_states = backward_curr_node.get_prev_states(feature_count)
        for node in backward_prev_states:
            node.get_accuracy()
            print(f"Using features ({node.subset}) accuracy is {node.accuracy:.2f} %")
            if node.accuracy > backward_best_accuracy:
                backward_best_accuracy = node.accuracy
                backward_curr_node = node

        print(f"Backward feature set was best {backward_curr_node.subset}, accuracy is {backward_curr_node.accuracy:.2f} %")
        if backward_curr_node.accuracy < backward_best_accuracy:
            print("(Warning Accuracy Decreased)")
            print(f"Finished Backward Search! The best feature subset is {backward_curr_node.subset}, accuracy is {backward_curr_node.accuracy:.2f} %")
            break

    final_best_subset = forward_curr_node.subset if forward_best_accuracy >= backward_best_accuracy else backward_curr_node.subset
    final_best_accuracy = max(forward_best_accuracy, backward_best_accuracy)
    print(f"Overall, the best feature subset is {final_best_subset}, with an accuracy of {final_best_accuracy:.2f} %")
    return

print("Welcome to Charles and Alan's Feature Selection Algorithm")
features = int(input("Please enter total number of features: "))
algo_option = int(input("Type the number on the algorithm you want to run: 1 for foward, 2 for backward, 3 for special: "))
print('\n')
if algo_option == 1:
    forward(features)            
if algo_option == 2:
    backward(features)
if algo_option == 3:
    forward_backward(features)
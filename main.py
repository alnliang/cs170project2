from node import Node 
import random
def forward(feature):
    trace = []
    best_accuracy = []
    curr_node = Node([])
    curr_node.get_accuracy()
    trace.append(curr_node)
    best_accuracy.append(curr_node)
    while len(curr_node.subset) != feature:
        curr_node.get_next_states(feature)
        for state in curr_node.next:
            state.get_accuracy()
            trace.append(state)
        curr_node = curr_node.get_highest_child_accuracy()
        best_accuracy.append(curr_node)
    return trace,best_accuracy

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
        
print("Welcome to Charles and Alan's Feature Selection Algorithm")
features = int(input("Please enter total number of features"))
algo_option = int(input("Type the number on the algorithm you want to run: 1 for foward, 2 for backward, 3 for special"))
if algo_option == 1:
    trace,best_accuracy = forward(features)
    print(len(trace))
    print(f"use no features and \"random\" evaluation, I get an accuracy of {trace[0].accuracy} %")
    print("Beginning Search")
    subset = 4
    best_acc_index = 1
    count = 0

    for i in range(1,len(trace)):
        count = count + 1
        print(f"Using features ({trace[i].subset}) accuracy is {trace[i].accuracy} %")
        if count == subset:
            print(f"Feature set was best {best_accuracy[best_acc_index].subset}, accuracy is  {best_accuracy[best_acc_index].accuracy}")
            count = 0
            subset = subset - 1
            if best_accuracy[best_acc_index].accuracy < best_accuracy[best_acc_index -1].accuracy:
                print("(Warning Accuracy Decreased)")
                print(f"Finished Search !! The best feature subset is {best_accuracy[best_acc_index -1].subset}, accuracy is  {best_accuracy[best_acc_index-1].accuracy}")
                break
            best_acc_index = best_acc_index + 1
                
    
if algo_option == 2:
    # trace = backward()
    # print(f"use all features and \"random\" evaluation, I get an accuracy of {trace[0].accuracy} %")
    backward(features)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#for the current test cases the first column is row 1 and row 2
from main import forward
from main import backward
from main import forward_backward

max = 10
a = [i for i in range(1, 10+1)]
x = np.asarray(a)
#forward examination
accuracies = []
for k in range(max):
    accuracies.append(forward(10, k))
y = np.asarray(accuracies)
plt.plot(x, y)
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()
print(accuracies)
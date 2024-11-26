import numpy as np


arr = np.array([5, 0, 2, 0])
print(np.mean(arr, keepdims=True, where=(arr!=0)))

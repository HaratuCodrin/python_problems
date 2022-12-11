import numpy as np

results = [
    [1.456,2.245,-3.441], 
    [4.53, 4.55, 1.22]
]

np.savetxt("results.txt", results)   # write

#read
result = np.loadtxt("results.txt")
print(result.tolist())
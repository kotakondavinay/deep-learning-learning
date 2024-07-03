import numpy as np
N = 1000000
M = 3
heads = np.zeros(M+1)
for i in range(N):
    flips = np.random.randint(0, 2, M) #generates M size array having the values between 0 & 2.
    h, _ = np.bincount(flips, minlength=2)
    heads[h] += 1
prob = heads / N
print("Probablities: %s", np.array2string(prob))
import numpy as np
counts = [1000, 10000, 100000, 1000000]
for count in counts:
    match = 0
    for j in range(count):
        a = np.random.randint(0, 365)
        b = np.random.randint(0, 365)
        if (a == b):
            match += 1
    print("Probability of a random match %0.6f" % (match/count,))
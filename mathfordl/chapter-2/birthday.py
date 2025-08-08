import numpy as np
for m in range(31, 40):
    matches = 0
    for n in range(100000):
        match = 0
        b = np.random.randint(0, 364, m)
        counts = np.bincount(b, minlength=364)
        for i in range(364):
            if (counts[i] > 1):
                match += 1
        if (match != 0):
            matches += 1
    print("%2d %0.6f" % (m, matches/100000))


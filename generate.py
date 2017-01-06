import sys
from collections import deque
import numpy as np
import random

def readFile(name):
    from scipy.io.wavfile import read
    return read(name)

def writeFile(num, data, name):
    from scipy.io.wavfile import write
    write(name, num, data)

def getSeeds(data, length):
    seeds = {}
    for idx in range(len(data)-length):
        seed = tuple(data[idx:idx+length])
        if not seed in seeds:
            seeds[seed] = deque([data[idx+length]])
        else:
            seeds[seed].append(data[idx+length])
    return seeds

def generate(seeds, length, seedslist):
    result = []
    key = getRandom(seedslist)
    result.extend(key)
    for i in range(1000000):
        if key not in seeds:
            key = getRandom(seedslist)
        result.append(random.choice(seeds[key]))
        key = tuple(result[0-length:])
    return np.array(result)

def getRandom(seedslist):
    return random.choice(list(seedslist))

def main(argv):
    length = 20
    if not len(argv) == 3:
        print('Error')
        return
    inputfile = argv[1]
    outputfile = argv[2]
    num, data = readFile(inputfile)
    print(0)
    seeds = getSeeds(data, length)
    print(1)
    result = generate(seeds, length, seeds.keys())
    print(2)
    writeFile(num, result, outputfile)

if __name__ == '__main__':
    main(sys.argv)

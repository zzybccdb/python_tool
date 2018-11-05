import matplotlib.pyplot as plt
import numpy as np 

f = open("reward.txt","r")
lines = f.readlines()
reward = []
y = []
for i, line in enumerate(lines):
    if( i % 1000 ):
        cut = line.find(":")+1
        reward.append(int(line[cut+1:]))
        y.append(i)
x = np.array(reward)
y = np.array(y)
plt.figure()
plt.plot(y,x)
plt.show()
f.close()
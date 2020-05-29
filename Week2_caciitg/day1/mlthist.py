import matplotlib.pyplot as plt 
import random
pop = [random.randint(21,130) for i in range(28)]
bins = [x for x in range(0,131,10)]

plt.hist(pop,bins,histtype='bar',rwidth=0.8)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Histogram')
plt.legend()
plt.show()
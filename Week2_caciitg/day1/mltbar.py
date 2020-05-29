import matplotlib.pyplot as plt 

x1 = [1,3,5,7,9]
y1 = [5,2,7,8,2]

x2 = [2,4,6,8,10]
y2 = [8,6,2,5,6]

plt.bar(x1,y1,label='Example One')
plt.bar(x2,y2,label='Example Two',color='g')
plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Info')
plt.show()
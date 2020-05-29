import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitscat',color='k',s=25,marker='o')

plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Scatter Plot')
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# xaxis = np.array([0,155])
# yaxis = np.array([0,56])
#
# plt.plot(xaxis,yaxis)
# plt.show()

# x = np.array([3,5,6,7,9])
# plt.plot(x,marker = 'o',ms = 20,mfc = 'green',mec = 'hotpink')
# plt.show()

# y = np.array([5,6,7,8])
# plt.plot(y,linestyle = 'dotted',color = 'green')
# plt.xlabel('Value')
# plt.ylabel('Total')
# plt.title("Data titile")
# plt.grid(axis=y)
# plt.grid()
# plt.show()
a = np.array([2,7,3,7,2,8,10])
b = np.array([4,5,1,2,7,8,3])
c = np.random.normal(2,33,333)

# plt.scatter(a,b,color = 'red')
# plt.bar(a,b,color = "red")
# plt.barh(a,b,color = 'hotpink')
# plt.bar(a,b,width=0.1)
# plt.hist(c)

d = np.array([33,22,55,66,77])
mylabels = ['apple','banana','mango','pineapple','graps']
plt.pie(d,labels=mylabels)

plt.legend(title = 'Five fruits')
plt.show()

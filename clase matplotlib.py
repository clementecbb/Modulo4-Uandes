import matplotlib.pyplot as plt
import numpy as np

y=[1,2,5,4,7,3,7,9,10]
x=[3,4,2,6,8,3,6,5,10]
plt.plot(x,y)
plt.show()



x= np.arange(0,10)
plt.plot(x,np.sin(x))
plt.show()

plt.bar([1,2,3,4,5,6],[1,3,3,9,8,6])
plt.show()
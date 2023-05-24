import matplotlib.pyplot as plt
import numpy as np

y=[1,2,5,4,7,3,7,9,10]
x=[3,4,2,6,8,3,6,5,10]
plt.plot(x,y)
plt.show()


#grafico lineal
x= np.arange(0,10)
plt.plot(x,np.sin(x))
plt.show()


#grafico de barras
plt.bar([1,2,3,4,5,6],[1,3,3,9,8,6])
plt.show()

#cordenadas polares
r= np.linspace(0,2*np.pi,500)
t=5*r

plt.polar(t,r)
plt.show()
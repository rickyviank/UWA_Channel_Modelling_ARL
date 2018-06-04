#import cmath as np
import matplotlib.pyplot as plt
#from cmath import sqrt
import numpy as np

m = (1500.0/1023)
n = (1539.0/1650)
x = np.linspace(0,360,100000)
y = np.absolute((m*np.cos(np.pi*x/180.0)-np.sqrt((n**2-(np.sin(np.pi*x/180.0))**2) + 0j))/(m*np.cos(np.pi*x/180.0)+np.sqrt((n**2-(np.sin(np.pi*x/180.0))**2) + 0j))) 
plt.plot(x,y)
plt.show()





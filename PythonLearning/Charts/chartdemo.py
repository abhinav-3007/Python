import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,100,10)
y = np.linspace(1,100,10)

plt.figure()

plt.subplot(2,2,1)
plt.title("x,y")
plt.plot(x,y,'r-')

plt.subplot(2,2,2)
plt.title("x**2,y**3")
plt.plot(x**2,y**3,'b+')

plt.subplot(2,2,3)
plt.title("x,y")
plt.plot(x,y,'r<')

plt.subplot(2,2,4)
plt.title("x**2,y**3")
plt.plot(x**2,y**3,'b+')

plt.show()

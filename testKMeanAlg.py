import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans


x= -2 * np.random.rand(100,2)
print (x)
x1 = 1 + 2 * np.random.rand(50,2)
x[50:100, :] = x1
plt.scatter(x[ : , 0], x[ :, 1], s = 50, c = 'b')
plt.show()
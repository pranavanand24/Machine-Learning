#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10)
y = x ^ 2
z = x ^ 3
t = x ^ 4
plt.title("Graph drawing")
plt.xlabel("Time")
plt.ylabel("distance")
plt.plot(x,y)

plt.annotate(xy=[2,1], s = 'Second Entry')
plt.annotate(xy=[4,6], s = 'Third Entry')


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10)
y = x ^ 2
z = x ^ 3
t = x ^ 4
plt.title("Graph drawing")
plt.xlabel("Time")
plt.ylabel("distance")
plt.plot(x,y)

plt.annotate(xy=[2,1], s = 'Second Entry')
plt.annotate(xy=[4,6], s = 'Third Entry')
# Adding Legends
plt.plot(x,z)
plt.plot(x,t)
plt.legend(['Race1', 'Race2','Race3'], loc=4)


# In[ ]:





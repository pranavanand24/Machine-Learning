#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import *
from pylab import *
x = linspace (-3,3,30)
y = x ** 2
plot (x,y)
show()


# In[4]:


from pylab import *
plot(x, sin(x))
plot(x, cos(x), 'r--')
plot(x, -sin(x), 'g--')
show()


# In[5]:


import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor ='y')
plt.plot(range(12))


# In[6]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(221, facecolor = 'y')
ax2.plot([1,2,3])


# In[2]:


import matplotlib.pyplot as plt
fig,a = plt.subplots(2,2)
import numpy as np
x = np.arange(1,5)
a[0][0].plot(x,x*x)
a[0][0].set_title('square')
a[0][1].plot(x, np.sqrt(x))
a[0][1].set_title('square root')
a[1][0].plot(x, np.exp(x))
a[1][0].set_title('exp')
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')
plt.show()


# In[ ]:





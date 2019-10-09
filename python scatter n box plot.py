#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.rand(10,5), columns = ['A','B','C','D','E'])
df.plot.box(grid = 'TRUE')


# In[15]:


import pandas as pd 
import numpy as np
df = pd.DataFrame(np.random.rand(50,4), columns = ['a','b','c','d'])
df.plot.scatter(x ='a', y = 'b')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = df)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
sns.pairplot(df, kind ="scatter")
plt.show()


# In[ ]:





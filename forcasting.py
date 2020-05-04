#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
wsb_df = pd.read_csv('wsb.csv')
wsb_df.head(10)


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


plt.figure(figsize=(10,4))
plt.xlabel("Month")
plt.ylabel("quantity")
plt.plot(wsb_df['Sale Quantity']);


# In[20]:


wsb_df.info()


# In[21]:


wsb_df['mavg_12'] = wsb_df['Sale Quantity'].rolling(window = 12).mean().shift(1)


# In[9]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)
wsb_df[['Sale Quantity', 'mavg_12']][36:]


# In[22]:


plt.figure(figsize=(10,4))
plt.xlabel("Months")
plt.ylabel("Quantity")
plt.plot(wsb_df['Sale Quantity'][12:])
plt.plot(wsb_df['mavg_12'][12:], '.')
plt.legend();


# In[23]:


import numpy as np

def get_mape(actual, predicted):
    y_true, y_pred = np.array(actual), np.array(predicted)
    return np.round(np.mean(np.abs((actual - predicted)/ actual))*100, 2)


# In[24]:


get_mape(wsb_df['Sale Quantity'][36:].values,
        wsb_df['mavg_12'][36:].values)


# In[25]:


from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(wsb_df['Sale Quantity'][36:].values,
                          wsb_df['mavg_12'][36:].values))


# In[32]:


wsb_df['ewm'] = wsb_df['Sale Quantity'].ewm(alpha = 0.2).mean()


# In[33]:


pd.options.display.float_format = '{:.2f}'.format


# In[34]:


wsb_df[36:]


# In[46]:


get_mape(wsb_df[['Sale Qunatity']][36:].values,
         wsb_df[['ewm']][36:].values)


# In[47]:


plt.figure(figsize=(10,4))
plt.xlabel("Months")
plt.ylabel("Quantity")
plt.plot(wsb_df['Sale Quantity'][12:])
plt.plot(wsb_df['ewm'])[12:], '.')
plt.legend()


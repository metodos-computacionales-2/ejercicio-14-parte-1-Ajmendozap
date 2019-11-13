#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pylab as plt


# In[8]:


data= np.loadtxt('data.dat')


# In[10]:


plt.plot(data[:,0],data[:,1])
plt.savefig('sin.png')
plt.show()


# In[ ]:





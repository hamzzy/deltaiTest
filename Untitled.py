#!/usr/bin/env python
# coding: utf-8

# In[33]:


def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n<=0) else n * factorial(n - 1);


# In[35]:


get_ipython().run_line_magic('timeit', 'factorial(5)')


# In[ ]:





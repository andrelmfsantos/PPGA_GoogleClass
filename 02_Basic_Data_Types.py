#!/usr/bin/env python
# coding: utf-8

# # Variables

# ## Object:
# 1. **None**
# 2. **Numbers**
#     * Integer
#     * Floating Point
#     * Complex
# 3. **Sequences**
#     * String
#     * Tuples
#     * Lists
# 4. **Keywords**:
#     * and, del, from, not, while, as, elif, global, else, if, pass, Yield, break...

# ## Operators:
#     * Arithmetic operators: +, -, *, /, **, //, %
#     * Assignment operators: =, +=, -=, *=, /=, %= **=, //=
#     * Logical operators: or, and, and not
#     * Relational operators: <, >, >=, !=,or, <>, and, ==

# # Exemplos

# In[15]:


andre = 2020.0


# In[22]:


doni = 2020


# In[23]:


print(type(andre), type(doni))


# In[10]:


type(andre)
type(doni)


# In[12]:


print('André: ', type(andre))
print('Doni:  ', type(doni))


# In[20]:


andre == doni 


# In[24]:


andre + doni 


# In[25]:


PPGA = andre + doni 


# In[26]:


print(PPGA)


# ## Library Maths
# [math](https://docs.python.org/2/library/math.html)

# In[27]:


import math


# In[28]:


fernanda = 2.67893


# In[29]:


math.ceil(fernanda)


# In[30]:


math.floor(fernanda)


# In[31]:


math.floor(2.67893)


#!/usr/bin/env python
# coding: utf-8

# # Strings

# In[1]:


meu_nome = 'André Santos'


# In[3]:


print(type(meu_nome))


# In[4]:


numero = 89


# In[5]:


n = '89'


# In[6]:


print(type(n), type(numero))


# In[7]:


numero + 10


# In[8]:


n + 10


# In[14]:


print(meu_nome[:5])


# In[15]:


print(meu_nome[-1])


# In[16]:


print(meu_nome[-2])


# In[22]:


print(meu_nome[-2:])


# In[20]:


print(meu_nome[1:3])


# In[23]:


len(meu_nome)


# In[24]:


print(meu_nome[11])


# In[27]:


len(meu_nome)-1


# In[28]:


print(meu_nome[len(meu_nome)-1])


# ## Resumo

# In[29]:


# Índice

# Positivo
#------------------------------------
# Index:  0 1 2 3 4 5 6 7 8 9 10 11
# String: A N D R É   S A N T O  S
#------------------------------------

# Negativo
#-------------------------------------------------
# Index:  -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# String:   A   N   D  R  É     S  A  N  T  O  S
#-------------------------------------------------

# Tamanho da str
# len(objeto)


# In[30]:


primeiro = "André "


# In[31]:


ultimo = "Santos"


# In[32]:


full_name = primeiro + ultimo
print(full_name)


# In[33]:


primeiro_numero = '19'


# In[34]:


segundo_numero = '07'


# In[35]:


primeiro_numero + segundo_numero


# # Lists

# In[36]:


alunos = ['André', "Doni", 'Eliane', 'Genesio']


# In[37]:


type(alunos)


# In[39]:


combinar = ['André', 25, "Doni", 45, 'Eliane', 35, 'Genesio', 56]


# In[40]:


vazia = []


# In[41]:


type(vazia)


# In[43]:


lista_de_lista = [1,[1,2],3]
type(lista_de_lista)


# In[44]:


lista_de_lista[1]


# In[45]:


combinar[4]


# In[46]:


combinar2 = ['André', 25, ["Doni", 45], 'Eliane', 35, 'Genesio', 56]


# In[47]:


combinar2[2]


# In[48]:


combinar[2]


# # Tuples

# In[51]:


tup1 = (2, 3)
type(tup1)


# In[52]:


(a, b) = tup1


# In[53]:


print(a)


# In[54]:


print(b)


# In[55]:


tup1[1]


# In[56]:


tup2 = (10, 25, 36, 45, 59, 60, 69)


# In[57]:


(c,d) = tup2[1:3]


# In[58]:


print(c,d)


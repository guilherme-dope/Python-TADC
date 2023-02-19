#!/usr/bin/env python
# coding: utf-8

# In[10]:


qcoca = 150
qpepsi = 130
valorcoca = 1.50
valorpepsi = 1.50
custo = 2500


# In[23]:


fatdiario = qpepsi * valorpepsi + qcoca * valorcoca


# In[24]:


fatanual = fatdiario * 12


# In[27]:


lucro = fatanual - fatdiario


# In[32]:


fatpepsi = qpepsi * valorpepsi


# In[31]:


print("O lucro anual foi de {} e o faturamento de pepsi foi de {}. " .format(lucro, fatpepsi))


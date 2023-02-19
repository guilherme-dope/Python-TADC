#!/usr/bin/env python
# coding: utf-8

# In[27]:


idbebida = input("Insira o código da bebida: ")


# In[41]:


if "BAC" in idbebida:
    print("True - Bebida com alcool")
elif "BEB" in idbebida:
    print("False - Bebida sem alcool")
else:
    print("Codigo Errado")


#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pywhatkit as pwt
pwt.text_to_handwriting("welcome","C:\\Users\\Administrator\\Desktop\\output.png",[10,10,10])


# In[5]:


import pywhatkit as pwt
fo=open("C:\\Users\\Administrator\\Desktop\\text.txt","r")
str=fo.read()
pwt.text_to_handwriting(str,"C:\\Users\\Administrator\\Desktop\\output.png",[10,10,10])


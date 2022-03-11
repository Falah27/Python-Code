#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2

imgloc = 'C:/Users/Administrator/Desktop/luffy.png'

img = cv2.imread(imgloc)
cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invgray = 255 - gray
cv2.imshow("gray", invgray)

blur = cv2.GaussianBlur(invgray, (21, 21), 0)
invblur = 255 - blur

sketch = cv2.divide(gray, invblur, scale=256.0)
cv2.imshow("sketch", sketch)

cv2.waitKey(0)


# In[ ]:





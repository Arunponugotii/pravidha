#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


year=int(input("Enter the year:"))
if year % 4 == 0 :
    if year % 100 ==0:
        if year % 400 == 0:
            print("it is a leaf year")
        else:
            print("it is not a leaf year 400")
    else:
        print("it is a leaf year")
else:
    print("it is normal year")


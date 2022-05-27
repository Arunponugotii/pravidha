#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BMI caluclator
weight=input("Enter the weight:")
height=input("Enter the height:")
bmi=round(int(weight) / float(height)**2,2)
if bmi < 18.5:
     print(f"Your BMI is {bmi}, you are under weight")
elif bmi >= 18.5 and bmi < 25:
    print(f"your BMI is {bmi},you are normal weight")
elif bmi >= 25 and bmi < 30:
     print(f" your BMI is {bmi}, you are over weight")
elif bmi >= 30 :
     print(f"Your BMI is {bmi},you are obey go hospital immidiatly")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


str1= "learnpythonprograaming"
str1.count("o")


# In[6]:


str1.count("o",1,12)  #str1[1:12].count("o")


# In[16]:


str2 = "learnpython"
str2.find("o")


# In[17]:


str2.rfind("o")


# In[21]:


str3 = "welcome to xyz learn python"
str3.find("xyz")


# In[22]:


# if somone changes the str3 then index will be changed then syntax is

str3 = "welcome to xyz learn python"
str3[str3.find("xyz"):]


# In[24]:


str3 = "welcome to xyz learn python"
str3.find("t")


# In[25]:


str3[8]


# In[26]:


str4 = "what we think we become we"


# In[28]:


a = str4.find("we")


# In[29]:


print(a)


# In[30]:


a = str4.find("we",a+1)


# In[31]:


print(a)


# In[49]:


str5 = "hello"


# In[63]:


str1 = "Hello welcome to the lets upgrade"

str1.lower()

str1.upper()

str1.title()

str1.swapcase()

str1.capitalize()

str2 = "@#@#@#intel@#@#@#"

str2.lstrip("@#")

str2.rstrip("@#")

str2.strip("@#")

str3 = "@#@#%%int%el@#@%#"

str3.strip("@#%")

str6 = "%hellow%"

str6.replace("%","")

str1 = "\t\thellow\t\t"

str1.strip()

str1= "mahesh"
str2 = "maheshrao"
str3 = "mahesh birajdar"

str1.ljust(10,"@")




# In[ ]:





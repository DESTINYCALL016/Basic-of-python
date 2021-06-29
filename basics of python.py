#!/usr/bin/env python
# coding: utf-8

# ###Basics of python
# 

# In[1]:


#string
'''elements of string can be exess by index
String can not be uptated by indexes'''


# In[2]:


a="ayush chaudhary"
a


# In[3]:


a[0]


# In[4]:


b=7
a[b]


# In[5]:


a[b]='c'


# In[6]:


#type() function cangive type of variable


# In[7]:


type(a)


# In[8]:


#'j' represent IOTA of complex  


# In[9]:


c=1-25j
type(c)


# In[10]:


#list
'''list is hetrogenous
elements are in [] brackets
elements can be excess by indexes
elements can be changed by indexes'''


# In[11]:


ayush_chaudhary=[0,10,1.54,"ayush chaudhary"]
ayush_chaudhary


# In[12]:


type(ayush_chaudhary)


# In[13]:


ayush_chaudhary[2]


# In[14]:


ayush_chaudhary[1]=2584
ayush_chaudhary[1]


# In[15]:


#reverse() function


# In[16]:


ayush_chaudhary.reverse()
ayush_chaudhary


# In[19]:


#'tuple' 
'''tuple is hetrogenous
elements can excess by indexes
elements can not be changed by indexes
can not be reversed

'''


# In[20]:


ayush_tuple=(2,65,2.15,"king of the hell")
ayush_tuple


# In[21]:


ayush_tuple[2]


# In[22]:


ayush_tuple[2]=245


# In[23]:


ayush_tuple.reverse()


# In[24]:


#dict
'''no two elements(no.s) have to be same whereas their values can be same
if two elemets are same the later element will the only one that counts
values only excess by elements not by indexes
dict can be uptaded as list

'''


# In[25]:


ayush_dict={1:"ayush",2:"first",1:"first",4 :"king of the heaven"}
ayush_dict


# In[26]:


type(ayush_dict)


# In[27]:


ayush_dict={1:"ayush",4:"first",3:"first",2 :"king of the heaven"}
ayush_dict


# In[28]:


ayush_dict[4]="king of the hell"
ayush_dict


# In[29]:


#Sets
'''sets{} 
can not  takes duplicates
arranged in such a way that first digit from left is smallest and then arrange in ascending order Strings comes last
can not be excess with indexes and can not be updated
'''


# In[30]:


ayush_set={24,2,.125,'ayush',2,54,645,1,25,25,25,1,25,2,15,2,15,2,52,5,}
ayush_set


# In[31]:


ayush_set[4]


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import style


# In[16]:


days = [1,2,3,4,5,6,7]
temp1 = [30,32,35,34,36,33,38]
temp2 = [32,36,35,34,31,33,35]
temp3 = [31,37,36,32,35,34,33]
plt.xlabel('Days',fontsize = 12)
plt.ylabel('Temprature',fontsize = 12)
plt.title('Temperature of Delhi,Mumbai,Patna',fontsize = 12)
plt.axis([0,8,28,40])
style.use('ggplot')
plt.grid(color = "r",linewidth = 1)
plt.plot(days,temp1,"ro-",label = "Delhi Temp")
plt.plot(days,temp2,"go-",label = "Mumbai Temp")
plt.plot(days,temp3,"bo-",label = "Patna Temp")
plt.legend(loc = 4)
plt.show()


# In[ ]:





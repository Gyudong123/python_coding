#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd


# In[101]:


x= np.linspace(0,2,1000)
y = np.sin(2*np.pi*x)
z = np.sin(2*np.pi*x)
ax0 = np.zeros(1000)
t = np.array([np.ones(100)*i for i in range(10)]).flatten()
df = pd.DataFrame({"time": t ,"x" : x, "y" : y, "z" : ax0})
df1 = pd.DataFrame({"time": t ,"x" : x, "y" : ax0, "z" : z})

def update_graph(i):
    y = np.sin(2*np.pi*(x - 0.01*i))
    z = np.sin(2*np.pi*(x - 0.01*i))
    graph._offsets3d = (x,ax0, z)
    graph1._offsets3d = (x, y, ax0)
    title.set_text('3D Test, time={}'.format(i))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

graph = ax.scatter(x, ax0, z)
graph1 = ax.scatter(x, y, ax0)
plt.show()


# In[26]:


from IPython.display import HTML


# In[103]:


ani = matplotlib.animation.FuncAnimation(fig, update_graph, interval = 200, blit = False)
HTML(ani.to_html5_video())


# In[ ]:





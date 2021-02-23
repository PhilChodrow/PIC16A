# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:41:09 2021

@author: micha
"""



#This is how you makea scatter plot in python
#we will learn this later
import numpy as np
from matplotlib import pyplot as plt

x=np.random.rand(100)
y=np.random.rand(100)

plt.scatter(x,y)

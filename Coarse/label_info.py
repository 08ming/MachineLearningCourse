# -*- coding: utf-8 -*-

import glob
import numpy as np
import matplotlib.pyplot as plt
file_list = glob.glob('./data/train/data/*.txt') 
file_sizes = []
for file in file_list:
    with open(file,"r") as f:
        file_sizes.append(len(f.read()))
plt.hist(x = file_sizes, bins = 20, color = 'steelblue', edgecolor = 'black', rwidth=0.7)
plt.show()
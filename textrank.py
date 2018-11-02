
import numpy as np

import pandas as pd

f =open('./text.txt','r')
index_dict = {}
count = 0
temp = []
names = []
for line in f:
    line = line.strip()
    name,had = line.split('=',1)
    names.append(name)
    index_dict[name]=count
    count+=1
    temp.append([x.strip() for x in had.split(',')])
matrix = np.zeros([count,count])
for i in range(len(temp)):
    for j in temp[i]:
        matrix[i][index_dict[j]]=1

value = np.sum(matrix,axis=1)
new_m = matrix.T/value[:,None]
new_m = new_m.T
ones = np.ones((count,1))

for i in range(200):
    
    ones = 0.15+np.dot(0.85*new_m,ones)
print(ones)
    

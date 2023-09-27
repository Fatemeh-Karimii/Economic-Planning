# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:44:52 2023

@author: Se7eN.CO
"""

from mip import *

import numpy as np

Year = [0, 1, 2, 3, 4, 5] 
Product = ["Coal", "Steel", "Transport"] 

c = np.array([[0.1, 0.1 , 0.2 , 0.6],[0.5, 0.1 , 0.1 , 0.3],[0.4 , 0.2 , 0.2 , 0.2]])
d = np.array([[0 , 0.1 , 0.2 , 0.4],[0.7 , 0.1 , 0.1 , 0.2],[0.9 , 0.2 , 0.2 , 0.1]])
e = np.array([[0,60 , 60 ,60, 60, 60],[0,60 , 60 ,60, 60 , 60],[0,30 , 30 ,30, 30 , 30]])
p = np.array([[300], [350], [280]])
q = np.array([[150], [80], [100]])

m = Model("Economic Plan")


s = [[m.add_var() for i in range(7)]for t in range (1,4)]    
y = [[m.add_var() for i in range(8)]for t in range (1,4)]
x = [[m.add_var() for i in range(7)]for t in range (1,4)]


for i in range(3):
    for t in range(6):
         m += x[i][t]+s[i][t] == xsum(c[i][j]*x[j][t+1] for j in range(3)) + xsum(d[i][j]*y[j][t+2] for j in range(3))+s[i][t+1]+e[i][t]
       
for i in range(3):
    for t in range(6):
          m += x[i][t] <= p[i][0] + sum(y[i][k] for k in range (t+1)) 

          
for i in range(3):
    
    m += x[i][0] + s[i][0] == q[i][0] 
        
                
m.objective = maximize(xsum(c[i][3] * x[i][t+1] for t in range(6) for i in range(3)) + xsum(d[i][3] * y[i][t+2] for t in range(6) for i in range(3))) 
          
m.optimize()
print(m.objective_value)
for i in range(3):
    for t in range(6):
      print("s[{}][{}]: {}".format(i, t, s[i][t].x))
      
for i in range(3):
   for t in range(2,7):
      print("y[{}][{}]: {}".format(i, t, y[i][t].x))

for i in range(3):
    for t in range(6):
      print("x[{}][{}]: {}".format(i, t, x[i][t].x))
      
      
print(m.objective_values)
for y in m.consters:
    if(c.pi > 1e-5):
        print(format(**locals()))
        print(end = "")
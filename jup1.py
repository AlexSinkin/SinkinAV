#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np  
import random as rnd  
  
n=10  
m=10  
  
arr = np.zeros((m,n))  
  
for i in range(m):  
    for j in range(n):  
        arr[i,j]=rnd.randint(2,75)  
print(arr)  
print('___________________________')  
          
for i in range(m):  
    for j in range(n):  
        if arr[i, j] % 2 != 0:  
            print(arr[i, j])  
            arr[i, j]= -1  
              
print('__________________________')  
  
print(arr) 


# In[23]:


import numpy as np 
import random as rnd 

n=rnd.randint(10,100) 

arr = np.zeros((n,n)) 

for i in range(n): 
    for j in range(n): 
        arr[i,j]=rnd.randint(1,100) 

print('Создать случаую квадратную матрицу') 
print(arr) 
print('___________________________') 

summ=0 
maximum=arr[1,1] 
for i in range(n): 
    for j in range(n): 
        summ += arr[i,j] 
        if arr[i, j] > maximum: 
            maximum = arr[i, j] 

print('Summ=',summ) 
print('Maximum=', maximum) 
print('__________________________') 

for i in range(n): 
    for j in range(n): 
        arr[i,j] = arr[i,j]/maximum 

print('Поделить каждый элемент на максимум') 
print(arr) 
print('___________________________') 

S=0 
for i in range(n): 
    for j in range(n): 
        S += arr[i,j] 
    for c in range(n): 
        arr[i,c] = arr[i,j]-S/n 
    S=0 

print('Отнять от каждой строки матрицы среднее по строке') 
print(arr) 
print('___________________________') 


maximum=0 
[a,b]=[0,0] 
for i in range(n): 
    for j in range(n): 
        if arr[i,j] > maximum: 
            maximum = arr[i,j] 
[a,b]=[i,j] 

arr[a,b] = -1 
print('Заменить максимальное значение на -1') 
print(arr)


# In[26]:


import numpy as np 
def NearestElement(arr,Num): 
    ind = (np.abs(arr-Num)).argmin() 
    return arr[ind] 

arr = np.random.random(10) 
print(arr, '\n') 

Num = 0.5 

print(NearestElement(arr, Num))


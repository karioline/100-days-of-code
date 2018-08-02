# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:38:54 2018

@author: Kari
"""
import math


num_system = ['A', 'B','C','D','E','F','G','H','I','J','K', 'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def newNumeralSystem(number):
    result = []
    num_index = -1
    for i in range(len(num_system)):
        if(number == num_system[i]):
            num_index = i
        #else:
         #   return []
    start_index = 0
    end = math.floor(num_index/2)
    i = num_index
    while ((i >= end) & (i >= start_index)):
        add = num_system[start_index] + " + "  + num_system[i]
        result.append(add)
        i = i-1
        start_index = start_index+1
    return result



"""
number = 'G'
result = []
num_index = -1
for i in range(len(num_system)):
    if(number == num_system[i]):
        num_index = i

print(num_index)
 
start_index = 0
end = math.floor(num_index/2)
i = num_index
while i >= end:
    add = num_system[start_index] + " + "  + num_system[i]
    result.append(add)
    print(result)
    i = i-1
    start_index = start_index+1
    
print(result)


def newNumeralSystem(number):
    result = []
    num_index = -1
    for i in range(len(num_system)):
        if(number == num_system[i]):
            num_index = i
        #else:
         #   return []
    start_index = 0
    for i in range(num_index, math.ceil(num_index/2)):
    if(num_index == start_index):
        add = num_system[start_index] + " + " + num_system[num_index]
        result.append(add)
    elif((num_index-start_index) == 1):
        add = num_system[start_index] + " + "  + num_system[num_index]
        result.append(add)
    else:
        add = num_system[start_index] + " + "  + num_system[num_index]
        result.append(add)
        start_index = start_index+1
  """          

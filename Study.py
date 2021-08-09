#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:31:43 2020

@author: susandas
"""
print("Hello World")

my_list=[1,2,3,4,5]
type(my_list)
my_tuple = (1,2,3)
print(my_list)

from itertools import combinations
from itertools import permutations 
import numpy as np
import math
arr=np.array(['H','O','R','S','E'])
print(len(list(combinations(arr, 2)) ))
print(len(list(permutations(arr,2) ))) 

import math
red=math.factorial(10)/((math.factorial(7))*math.factorial(3))
blue=math.factorial(8)/((math.factorial(3))*math.factorial(5))
print(red*blue)


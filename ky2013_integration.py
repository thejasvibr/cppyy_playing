# -*- coding: utf-8 -*-
"""
Completing the Python-Cpp link for KY2013
=========================================
"""

import cppyy

#cppyy.include('../combineall_cpp_python/combineall_cpp/set_operations.h')
#cppyy.include('../combineall_cpp_python/combineall_cpp/combineall.h')
#cppyy.include('../combineall_cpp_python/combineall_cpp/set_operations.h')
#cppyy.include('../combineall_cpp_python/combineall_cpp/combineall.h')
cppyy.include('../combineall_cpp_python/combineall_cpp/checking_combineall.cpp')
from cppyy.gbl.std import vector, set

# initalise a vector of vectors
acc = vector[vector[int]]([[ 0, 1, 0, 0,-1,-1], 
			   [1, 0, 1, 1, 0, 1],
			   [0, 1,  0,-1, 1,  0],
			   [0, 1, -1, 0,-1,  0],
			   [-1, 0, 1,-1, 0, 1],
			   [-1, 1, 0, 0, 1, 0]]);

#acc = ([[1,0,1],[1,0,1],[1,0,1]])

# initialise a set of nodes
Vt = set[int](range(5))
l = set[int]([])

## run the get_Nvl function
# compat = cppyy.gbl.get_Nvl(acc, Vt, l)
#print(compat)
#print('Module executed')

X = set[int]([])
# run combineall 
solutions = cppyy.gbl.combine_all(acc, Vt, l, X)
print('solutions are:',solutions)

#%% Load a given 'flatA.txt' file and convert it into a vector<vector<int>>
import numpy as np 
print('loading flatA.txt...')
aa = np.loadtxt('..\\..\\..\\research_repos\\pydatemm\\ky2012\\flatA.txt')
Ac = aa.reshape(int(np.sqrt(aa.shape[0])),-1)
Ac = np.asarray(Ac, dtype='int32')
Ac = Ac[:300,:300]
print('...done loading flatA.txt')
# now make Ac into a vector<vector<int>>
#%% 
print('Starting CombineAll cppyy run...')
n_rows = Ac.shape[0]
ac_cpp = vector[vector[int]]([Ac[i,:].tolist() for i in range(n_rows)])
v_cpp = set[int](range(n_rows))
l_cpp = set[int]([])
x_cpp = set[int]([])
soln_cpp = cppyy.gbl.combine_all(ac_cpp, v_cpp, l_cpp, x_cpp)
print('Done and solutions are:', soln_cpp)
print('Ended cppyy CombineAll run')

ff = np.random.normal(0,1,2000)

# convert all vector<vector<int>> back to list of lists
for i, each in enumerate(soln_cpp[:100]):
    print(ff[each])
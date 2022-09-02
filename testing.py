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
compat = cppyy.gbl.get_Nvl(acc, Vt, l)
print(compat)
print('Module executed')

X = set[int]([])
# run combineall 
#solutions = cppyy.gbl.combine_all(acc, Vt, l, X)
#print('solutions are:',solutions)

# run check combineall 
cppyy.gbl.main()



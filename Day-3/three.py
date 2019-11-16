import numpy as np

a = np.array([(1,2,3),(4,5,6)])

# to find the number of dimensions of the array
print(a.ndim)

# to find the itemsize
print(a.itemsize)

# to find the array data type
print(a.dtype)

# to find the array size
print(a.size)

# to find the shape of an array
print(a)
print(a.shape)


# to reshape an array
a = np.arange(24)
print(a)
a = a.reshape(2,4,3)
print(a) 

# to slice an array
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(a[0:2,0])

# to print a numbers spaced between values
a = np.linspace(1,3,5)
print(a)

a = np.array([2,4,6])
print(a.max())
print(a.min())
print(a.sum())

# axis calculation
a = np.array([(1,2,3),(4,5,6)])
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))

a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# vertical stacking
print(np.vstack((a,b)))

# horizontal stacking
print(np.hstack((a,b)))

# join an array values into a single one
print(a.ravel())

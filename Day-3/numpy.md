## Numpy

**NumPy** is a Python package. It stands for **'Numerical Python'**. It is a library consisting of multidimensional array objects and a collection of routines for processing of array.

Using **NumPy**, a developer can perform the following operations

* Mathematical and logical operations on arrays.

* Fourier transforms and routines for shape manipulation.

* Operations related to linear algebra. NumPy has in-built functions for linear algebra and random number generation.

The most important object defined in **NumPy** is an **N-dimensional array** type called **ndarray**. It describes the collection of items of the same type. Items in the collection can be accessed using a zero-based index.

Every item in an ndarray takes the same size of block in the memory. Each element in ndarray is an object of data-type object (called **dtype**).

Any item extracted from ndarray object (by slicing) is represented by a Python object of one of array scalar types. The following diagram shows a relationship between ndarray, data type object (dtype) and array scalar type - ndarray

<div style="text-align:center">
    <img src="ndarray.jpg" />
</div>

```
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

#### object
Any object exposing the array interface method returns an array, or any (nested) sequence.

#### dtype
Desired data type of array, optional

#### copy
Optional. By default (true), the object is copied

#### order
C (row major) or F (column major) or A (any) (default)

#### subok
By default, returned array forced to be a base class array. If true, sub-classes passed through

####  ndmin
Specifies minimum dimensions of resultant array
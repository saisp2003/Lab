import numpy as np

# arr=np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)])

# print(arr)

# py_list=[1,2,3]
# print("python list muliplication:",py_list*3)


# py_list=np.array([1,2,3])
# print("numpy array multiplication:",py_list*3)



# arr=np.zeros((3,3))
# print(arr)

# arr=np.ones((3,3))
# print(arr)

# arr=np.eye(3)
# print(arr)

# arr=np.arange(0, 10, 2)
# print(arr)   

# arr=np.full((3, 3), 5)
# print(arr)

# arr=np.random.rand(6,7)*100
# print(arr)


# arr=np.random.randint(5,size=(2,3))
# print(arr)
arr1 = [1.9, 2.8, 3.1, 9.6, 4.5]
arr = np.array(arr1).astype(float)
# print(arr)

# arr.tolist()

# print(arr.tolist())

# arr.size
# print(arr.size)

# arr.shape
# print(arr.shape)

# arr.dtype
# print(arr.dtype)

# np.copy(arr)
# arr2 = arr.copy()
# print(arr2)

# arr.view(float)
# print(arr.view(float))

# arr.sort()
# print(arr)

# arr.reshape(5, 1)
# print(arr.reshape(5, 1))

# arr.resize((5,6))
# print(arr)
#give an example of append in numpy
#arr_appended = np.append(arr, [7, 8, 9])
# print(arr_appended)


# arr_insert=np.insert(arr,2,[7,8,9])

# print(arr_insert)

# np.delete(arr,3,axis=0) 
# print(arr)

# arr_concatenate=np.concatenate((arr,arr_appended),axis=0)
# print(arr_concatenate)
# arr_split=np.array_split(arr,2)
# print(arr_split)

# arr_hsplit=np.hsplit(arr,5)
# print(arr_hsplit)

# print(arr[1])

# arr[1] = 4
# print(arr)

# arr_slice=print(arr[0:3])


# arr_slice_1=print(arr[:2])
   

# arr_condition = arr < 5
# print(arr_condition)

# print(~arr_condition)

# print(arr[arr<5])

# print(np.add(arr,1))

# print(np.subtract(arr,2))

#print(np.multiply(arr,5))

# print(np.divide(arr,4))

# print(np.power(arr,5))

#print(np.sqrt(arr))

#print(np.sin(arr))

#print(np.log(arr))

#print(np.abs(arr))

#print(np.ceil(arr))

# print(np.floor(arr))

# print(np.round(arr))

#print(np.mean(arr,axis=0))

# print(arr.sum())

# print(arr.min())

# print(arr.max(axis=0))

#print(np.var(arr))

#print(np.std(arr,axis=0))


# arr2=np.array([(1,8,9,54)])
# arr3=np.array([(2,3,4,5)])
# print(np.corrcoef(arr2,arr3))

array_1d=np.array([1,2,3,4,5])
array_2d=np.array(([1,2,3],[4,5,6]))

print(array_2d.max(axis=1))





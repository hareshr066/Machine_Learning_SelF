import numpy as np
np.random.seed(42)
data=np.random.randint(10,101 , size=(10,5))

# level = 1
#1
print(data)
print(np.shape(data))
print(np.ndim(data))
print(np.size(data))
print(data.dtype)
#2 indexing
print(data[0,:])
print(data[-1,:])
print(data[:,0])
print(data[:,-1])
print(data[4][2])
#3 slicing
print(data[0:3])
print(data[7:10])
print(data[:,0:2])
print(data[:,3:5])
print(data[:3,-2:])
print(np.prod(data[:3,-2:]))  # for multiplying
#4 vectorization
print(np.minimum(data+5,100)) #adding bonus,and if the bonus exceeds the 100 then 100 will be given
print(np.mean(data,axis=1))
print((data-np.mean(data,axis=0))/np.std(data,axis=0))
#5 boolean indexing
print(data[data>=50])
print(np.sum(data>=50))



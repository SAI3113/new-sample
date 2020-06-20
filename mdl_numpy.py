import numpy as np
#             2d shape
# a = np.array([1,2,3])
# b = np.array([[0.2,0.35,1.87],[1.5,2,3.78]],dtype='float64')
# print(b.ndim,b.shape,b.dtype,b.size,b.itemsize)
# total_size= b.size*b.itemsize   #   =b.nbytes
# print(total_size)
# print(b.nbytes)
# a = np.array([[1,2,3,4,5,7],[15,22,14,5,23,18]])
# print(a[0,1])
# print(a[-1,-2])
# print(a[:,2])
# print(a[0,:])
# print(a[0,1:5])
# print(a[0,1:5:2])  #[raw,colons:steps]
# a[1,4]=21
# a[1,1:4]=[16,20,31]
# a[:,5]=6
#             3d shape
# b = np.array([[[1,2],[3,4]],[[5,6],[7,9]]])
# print(b[1,0,:])
# b[1,1,1]=8
# b[:,1,:]=[[9,9],[8,8]]
# print(b)
#            initializing
# a = np.zeros((2,2),dtype='int32')
# print(a)
# b= np.ones((3,3,3))
# print(b)
# c = np.full((2,3),311,dtype='float32')
# print(c)
# d = np.full_like(a,5,dtype='float16')
# print(d)
# e = np.random.randint(0,10,(2,3))
# print(e)
# f = np.random.rand(2,3)
# print(f)
# g = np.random.random_sample(a.shape)
# print(g)
# h = np.identity(3)
# print(h)
# i = np.array([[[[1,2,3]]]])
# i_ =np.repeat(i,5,axis=1)    #0=1d  1=2d  2=3d ...
# print(i_)

#     ex
# ex = np.ones((5,5))
# ex[1:4,1:4]=0
# ex[2,2]=9
# print(ex)

# b = a is wrong
# b = a.copy()is correct

#       math
# a = np.array([1,2,3,4,5])
# print(a+2)
# print(a-2)
# print(a*2)
# b = np.array([1,2,3,4,5])
# print(a*b)
# print(a**2)
# print(np.sin(a),np.cos(a))
#     linear algebra
# a = np.ones((3,2))
# b = np.full((2,3),2)
# print(np.matmul(a,b))  #a(x1,y1)*b(x2,y2)  y1 must equals x2
# print(np.matmul(b,a))  #b(x1,y1)*a(x2,y2)  y1 must equals x2
# a = np.identity(2)
# print(np.linalg.det(a))         #Determinant:For a 2×2 matrix (2 rows and 2 columns) the determinant is easy: ad-bc
#       statistics
# stats1 = np.array([1,2,3,4,5])
# print(np.min(stats1))
# print(np.max(stats1))
# stats2= np.array([[1,2,3,4,5,7],[15,22,14,5,23,18]])
# print(np.min(stats2,axis=0))
# print(np.max(stats2,axis=0))
# print(np.sum(stats1))
# print(np.sum(stats2,axis=0))
#        reorgnizing arrays
# bfr = np.array([[1,2,3,4],[5,6,7,8]])
# print(bfr)
# aftr = bfr.reshape((4,2))  #same size only
# print(aftr)
# aftr = bfr.reshape((2,2,2))
# print(aftr)
# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# c = np.vstack([a,b])  #vertical stack
# print(c)
# c = np.vstack([a,a,b,b])
# c = np.hstack([a,b])  #horizantal stack
# print(c)
# c = np.hstack([a,a,b,b])
# print(c)
# a = np.zeros((2,3))
# b = np.ones((2,3))
# c = np.hstack([a,b])
# print(c)
# c = np.vstack([a,b])
# print(c)
#       Load data in from a file
# a = np.genfromtxt('data.txt',delimiter=',')  data.text=array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27]])
# print(a)
# a = a.astype('int32')  #to convert text data to integers
#       Advanced Indexing and Boolean Masking
# a = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27]])
# print(a>5)  #true or false
# print(a[0,[0,5,6]])   #you can index a list
# print(a[a>5])
# print(np.any(((a<10) & (a>5)),axis=0))   #if_there_is_any(condition,location)   true or false
# print(np.all(a>10,axis=0))   #are_all(condition,location)   true or false
"""
search for numpy.arrange() & numpy.linespace() & numpy.loadfile(#or loadtext#)()
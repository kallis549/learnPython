import numpy as np

my_list = [1,2,3]
print (my_list)

arr = np.array(my_list)
print (arr)


my_mat = [[1,2,3],[4,5,6], [7,8,9]]
print (my_mat)

x = np.zeros((5,5))
x[3,4]=23424

print (x)

print(np.zeros((4,4)))
print(np.zeros((5)))
print(np.arange(3,12,1))
print(np.ones((5,6)))

print(np.linspace(0,5,20))
print(np.eye(7,7))
print(np.random.rand(7,7))

print(np.random.randint(5,12312312,20))

arr = np.arange(35)
arr1 = arr.reshape(5,7)
print(arr1)
print(arr1.shape)

ranarr = np.random.randint(0,50,10)
print(ranarr)
print(ranarr.max())
print(ranarr.min())

print(ranarr.argmax())
print(ranarr.argmin())


arr = np.arange(0,11)
arr[0:5] = 100
print (arr[:6])
print (arr[1:6])
print (arr)
print (arr[5:])

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print (arr_2d[2:3])
print (arr_2d[:2,1:])


## CONDITIONAL SELECTION
an_arr = np.arange(1,25)
bool_arr = an_arr > 15
print (bool_arr)
print (an_arr[an_arr > 15])


print ("***********RESHAPE")
a_arr = np.arange(50)
print (a_arr)
a_arr = np.arange(50).reshape(5,10)
print (a_arr)
print (a_arr + 5)
print (a_arr * 5)

### NUMPY EXERCISES
#### Create an array of 10 zeros 
the_arr = np.zeros(10)
print (the_arr)

##Create an array of 10 ones
the_arr = np.ones(10)
print (the_arr)

#### Create an array of 10 fives
the_arr = the_arr + 4
print (the_arr)

#### Create an array of the integers from 10 to 50
the_arr = np.arange(10,51,1)
print (the_arr)

#### Create an array of all the even integers from 10 to 50
the_arr = np.arange(10,51,2)
print (the_arr)

the_arr = np.arange(11,51,2)
print (the_arr)

#### Create a 3x3 matrix with values ranging from 0 to 8
the_arr = np.arange(0,9)
print (the_arr.reshape(3,3))

#### Create a 3x3 identity matrix
print(np.eye(3))

#### Use NumPy to generate a random number between 0 and 1
thearr = np.random.rand(1)
print (thearr)

#### Use NumPy to generate an array of 25 random numbers 
## sampled from a standard normal distribution
thearr = np.random.rand(25)
print (thearr)

#### Create the following matrix:
# array([[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ],
#       [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 ],
#       [0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 ],
#       [0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 ],
#       [0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 ],
#       [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6 ],
#       [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7 ],
#       [0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8 ],
#       [0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9 ],
#       [0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.  ]])
thearr = np.arange(0.01,1.01,0.01).reshape(10,10)
print (thearr)

#### Create an array of 20 linearly spaced points between 0 and 1:
thearr = np.arange(0,1,0.05)
print (thearr)

## Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to 
# replicate the resulting matrix outputs:
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# array([[12, 13, 14, 15],
#       [17, 18, 19, 20],
#       [22, 23, 24, 25]])
thearr = np.arange(1,26,1).reshape(5,5)
print (thearr)
print (thearr[2:, 1:])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# 20
print (thearr[3:4][0][4])


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# array([[ 2],
#       [ 7],
#       [12]])
print (thearr[:3,1:2])

# array([21, 22, 23, 24, 25])
print (thearr[4:,:][0])


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# array([[22, 23, 24, 25]])
print (thearr[4:,1:])


##Q1
## a)
import random
import time


rows,cols=(5,5)

array_q1_a=[[0 for j in range (cols)] for i in range(rows)]

for i in range (0,rows):
    for j in range (0,cols):
        array_q1_a[i][j]=random.random();

print(array_q1_a)

##b)

def create_array(rows,cols):
    array=[[0 for j in range (cols)] for i in range(rows)]

    for i in range(0,rows):
        for j in range (0,cols):
            if i==j:
                array[i][j]=1
                
    return array

rows = int(input("\nRows : "))
cols = int(input("\nColumns : "))
result_Q1_b=create_array(rows,cols)
print(result_Q1_b)

##c)
def multiply_matrices(row1,col1,row2,col2):
    if col1!=row2 or col1==0 or row1==0 or row2==0 or col2==0 :
        print("can not multiply these two matrices")
    else:
        array1=[[0 for j in range (col1)] for i in range(row1)]
        array2=[[0 for j in range (col2)] for i in range(row2)]

        result=[[0 for j in range (col2)] for i in range(row1)]

        print("Matrix 1")
        for i in range(0,row1):
            for j in range(0,col1):
                array1[i][j]=int(input("value for {} {} : ".format(i,j)))

        print("\nMatrix 2")

        for i in range(0,row2):
            for j in range(0,col2):
                array2[i][j]=int(input("value for {} {} : ".format(i,j)))

        ##result
        for i in range(0,row1):
            for j in range(0,col2):
                for k in range(0,row2):
                    result[i][j] += array1[i][k] * array2[k][j]

        return result
    
row1 = int(input("\nRows for matrix 1 : "))
col1 = int(input("\nColumns for matrix 1 : "))
row2 = int(input("\nRows for matrix 2 : "))
col2 = int(input("\nColumns for matrix 2 : "))
result_Q1_c=multiply_matrices(row1,col1,row2,col2)
print("\nResult\n",result_Q1_b)


##d)
start_time=time.time()
result_Q1_d=multiply_matrices(row1,col1,row2,col2)
stop_time=time.time()
execution_time_q1_d=stop_time-start_time
print("\nExecution time for multiply two matrices : ",execution_time_q1_d)



########################################################################################

##Q2
import numpy as np

##a)
q2_a1=np.zeros(10)
print(q2_a1)

q2_a2=np.array([0]*10)
print(q2_a2)

#b)
array_q1_a_=np.array(array_q1_a)
print(array_q1_a_)

result_Q1_b_=np.array(result_Q1_b)
print(result_Q1_b)

result_Q1_c_=np.array(result_Q1_c)
print(result_Q1_c)

#c)
def multiply_matrices(array1,array2):
    if len(array1[0])!=len(array2) :
        print("column 1 and row 2 should be the same to multiply these two matrices")
    else:        
        print("Matrix 1")
        for i in range(0,row1):
            for j in range(0,col1):
                array1[i][j]=int(input("value for {} {} : ".format(i,j)))

        print("\nMatrix 2")

        for i in range(0,row2):
            for j in range(0,col2):
                array2[i][j]=int(input("value for {} {} : ".format(i,j)))

        ##result
        array1=np.array(array1)
        array2=np.array(array2)

        result=np.dot(array1,array2)

        return result

row1 = int(input("\nRows for matrix 1 : "))
col1 = int(input("\nColumns for matrix 1 : "))
row2 = int(input("\nRows for matrix 2 : "))
col2 = int(input("\nColumns for matrix 2 : "))

q2_c_array1=[[0 for j in range (col1)] for i in range(row1)]
q2_c_array2=[[0 for j in range (col2)] for i in range(row2)]

start_time=time.time()
result_Q2_c=multiply_matrices(q2_c_array1,q2_c_array2)
stop_time=time.time()
execution_time_q2_c=stop_time-start_time

print("\nResult\n",result_Q2_c)
print("\nExecution time for multiply two matrices : ",execution_time_q2_c)


#d)
def matrix_addition(array1,array2):
    if len(array1)!=len(array2) or len(array1[0])!=len(array2[0]) :
        print("can not add this two matrices")
    else:        
        ##result
        array1=np.array(array1)
        array2=np.array(array2)

        result=np.add(array1,array2)

        return result

def matrix_subtraction(array1,array2):
    if len(array1)!=len(array2) or len(array1[0])!=len(array2[0]) :
        print("can not subtract this two matrices")
    else:        
        ##result
        array1=np.array(array1)
        array2=np.array(array2)

        result=np.subtract(array1,array2)

        return result

result_Q2_d_addition=matrix_subtraction(q2_c_array1,q2_c_array2)
print("\nResult\n",result_Q2_d_addition)

result_Q2_d_subtraction=matrix_subtraction(q2_c_array1,q2_c_array2)
print("\nResult\n",result_Q2_d_subtraction)

#e)
e=np.array([4,7,9,-1,3,5,8],dtype=int)

print("Max : ",np.max(e))
print("Min : ",np.min(e))
print("summation of array :",np.sum(e))


#f)
min=e[0]
for i in e:
    if i<min:
        min=e[i]
        min_index=i

print("index of minimum value : ",min_index)

#g)
array_A=np.arange(5,23,2)
print(array_A)

#h)
array_B=np.linspace(5,9,9)
print("\n",array_B)

#i)
array_B=array_B.reshape(3,3)
print("\n",array_B)

#j)
array_j=np.cos(array_A)
print("\n",array_j)

#k)
exp=np.exp(array_A)
print("\n",exp)

#l)
l=array_A[2:6]
print("\n",l)

#m)
print("\n",array_B[:,1])

#n)
n_array1=np.random.rand(4)
n_array2=np.random.rand(4)

# Stacking the two arrays along axis 0
array_c1 = np.stack((n_array1, n_array2), axis = 0)
print ("stacked array along horizontal :\n ", array_c1)
  
# Stacking the two arrays along axis 1
array_c2 = np.stack((n_array1, n_array2), axis = 1)
print ("\nstacked array along vertical :\n ", array_c2)

#o)
split_c1_h=np.hsplit(array_c1,2)
print("\nSplit the array_c1 into 2 sub arrays again horizontally :\n",split_c1_h)

split_c1_v=np.vsplit(array_c1,2)
print("\nSplit the array_c1 into 2 sub arrays again vertically :\n",split_c1_v)

split_c2_h=np.hsplit(array_c2,2)
print("\nSplit the array_c2 into 2 sub arrays again horizontally :\n",split_c2_h)

split_c2_v=np.vsplit(array_c2,2)
print("\nSplit the array_c2 into 2 sub arrays again vertically :\n",split_c2_v)


########################################################################################

#Q3
import matplotlib.pyplot as plt

#a)
x=np.array(np.arange(0,np.pi/2,0.1))
print(x)

#b)
y=np.array((5*np.sin(x))-12)

#c)
t=np.array(np.arange(0,5,0.1))

#d)
f=np.array((2*t)+3)
plt.plot(x,y, label='y = 5 ∗ sin(x) − 12',color='red')
plt.plot(t,f, label='f = 2t + 3',color='blue')
plt.legend()
plt.show()


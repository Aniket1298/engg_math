import numpy as np
def scalar():
    print("Scalar multiplication is the multiplication of a vector by a scalar (where the product is a vector), and must be distinguished from inner product of two vectors (where the product is a scalar)")
    print("For example consider a Matrix A and a scalar value k given below")
    A=np.array([[2,4],[4,3]])
    print ("A \n",A)
    print ("k=3")
    print ("Now The scalar multiplication of the matrix A with k is")
    A=3*A
    print (A)
    n=int(input("Now Enter number of rows of matrix for matrix multiplication:"))
    A=[]
    for i in range(n):
        row=list(map(int,input().split()))
        A.append(row)
    k=int(input("Enter a value for scalar multiplication with the Matrix:"))
    A=np.array(A)
    A=k*A
    print ("Resultant matrix Ak is \n",A)
    
scalar()    

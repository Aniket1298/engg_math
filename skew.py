import numpy as np
def skew():
    print("In linear algebra, a skew-symmetric (or antisymmetric or antimetric[1]) matrix is a square matrix whose transpose equals its negative. That is, it satisfies the condition")
    print("\tAT=-A     where AT is Transpose Matric of A")
    print("For Example")
    A=np.array([[0,2,-5],[-2,0,-4],[5,4,0]])
    print ("Matrix A")
    for row in A:
        print (row,)
    print ("Matrix -A")
    for row in -A:
        print (row,)
    print ("Transpose of the matrix")
    for row in np.transpose(A):
        print (row,)
    print("Since AT=-A so the A is a Skew Symmetric Matrix")
    n=int(input("Now to Check Whether a Matrix is skew symmetric or not Enter numner of rows:"))
    matrix=[]
    print ("Enter Matrix Rowwise")
    for i in  range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    A=np.array(matrix)
    for row in -A:
        print (row,)
    print ("Transpose of the matrix")
    for row in np.transpose(A):
        print (row,)
    if False not in (-A==A.transpose()):
        print("Since AT=-A so the A is a Skew Symmetric Matrix")
    else:
        print("Since AT!=-A so the A is not a Skew Symmetric Matrix")
skew()

import numpy as np
def symmetry():
    print("In linear algebra, a symmetric matrix is a square matrix that is equal to its transpose. Formally, Because equal matrices have equal dimensions, only square matrices can be symmetric")
    print("If A is NxN Square Matrix then for A to be a Symmetric matrix it should hold A=AT where AT is Transpose Matrix of A")
    print("For Example           [1,7,3 ]")
    print("                    A=[4,7,-5]")
    print("                      [3,-5,6]")
    print ("So Transpose of Matrix A i.e AT is [1,7,3 ]")
    print ("                                   [4,7,-5]")
    print ("                                   [3,-5,6]")
    print ("Since A=AT so A is a symmmetric Matrix")
    print ("Now You can Check whether a Matrix is Symmetric or not")
    n=int(input("Enter Number of rows of the Square Matrix:"))
    print("Enter The Matix Rowwise")
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    A=np.array(matrix)
    AT=A.transpose()
    print ("Transpose of the matrix")
    for row in AT:
        print (row)
    if False not in (A==AT):
        print ("The given Matrix is a Symmetric Matrix")
    else:
        print ("The given Matrix is not a Symmetric Matrix")
symmetry()

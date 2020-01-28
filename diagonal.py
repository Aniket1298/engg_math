import numpy as np
def diagonal():
    print("In linear algebra, a diagonal matrix is a matrix in which the entries outside the main diagonal are all zero; the term usually refers to square matrices. An example of a 2-by-2 diagonal matrix is, while an example of a 3-by-3 diagonal matrix is")
    print("For Example           [1,0,0 ]")
        print("                    A=[0,7,0]")
        print("                      [0,-5,0]")
    print ("Now You can Check whether a Matrix is Diagonal or not")
    n=int(input("Enter Number of rows of the Square Matrix:"))
    print("Enter The Matix Rowwise")
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    A=np.array(matrix)
    zero=np.count_nonzero(A - np.diag(np.diagonal(A)))
    if zero==0:
        print ("The given Matrix is a Diagonal Matrix")
    else:
        print ("The given Matrix is not a Diagonal Matrix")
symmetry()
    

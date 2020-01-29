import numpy as np
def dot():
    print("In matrix multiplication, each entry in the product matrix is the dot product of a row in the first matrix and a column in the second matrix.\nn order for matrix multiplication to be defined, the number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    print ("For Example consider to metrices A(3x2) and B(2x4)")
    print ("\t  [1 3]\t\tB=[1 3 2 2]")
    print ("\tA=[2 4]\t\t  [2 4 5 1]")
    print ("\t  [2 5]\t\t")
    A=[[1,3],[2,4],[
        2,5]]
    B=[[1,3,2,2,],[2,4,5,1]]
    A=np.array(A)
    
    B=np.array(B)
    print ("\t\tResultant of A.B")
    C=np.dot(A,B)
    print (C)
    print("Now to Enter Two Metrices for Dot multiplication")
    n,m=list(map(int,input("Enter Dimension of First Matrix:").split()))
    A=[]
    print ("Enter First Matrix rowwise")
    for i in range(n):
        row=list(map(int,input().split()))
        A.append(row)
    r,s=list(map(int,input("Enter Dimension of Second Matrix:").split()))
    B=[]
    for i in range(r):
        row=list(map(int,input().split()))
        B.append(row)
    if m==r:
        print ("\t\tResultant of A.B")
        C=np.dot(A,B)
        print (C)
    else:
        print("Number of columns of first matrix should be equal to number of rows of Second Matrix")
    
        
dot()

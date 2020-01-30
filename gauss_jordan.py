import numpy as np
def gauss_jordan():
    print ("Gaussian elimination, also known as row reduction, is an algorithm in linear algebra for solving a system of linear equations. It is usually understood as a sequence of operations performed on the corresponding matrix of coefficients")
    print("To perform row reduction on a matrix, one uses a sequence of elementary row operations to modify the matrix until the lower left-hand corner of the matrix is filled with zeros, as much as possible. There are three types of elementary row operations:")
    print("Swapping two rows")
    print("Multiplying a row by a nonzero number")
    print("Adding a multiple of one row to another row")
    print("Using these operations, a matrix can always be transformed into an upper triangular matrix, and in fact one that is in row echelon form. Once all of the leading coefficients the leftmost nonzero entry in each row are 1, and every column containing a leading coefficient has zeros elsewhere, the matrix is said to be in reduced row echelon form. This final form is unique\n in other words, it is independent of the sequence of row operations used")
    print("For Example Consider the system of linear equation")
    print("x+y+z=3\n2x+3y+7z\nx+3y-2z=17\nAugmented Matrix")
    A=[[1,1,1,3],[2,3,7,0],[1,3,-2,17]]
    A=np.array(A)
    print (A)
    print ("\nR2->R2-2*R1")
    A[1]=A[1]-2*A[0]
    print(A)
    print ("\nR3->R3-R1")
    A[2]=A[2]-A[0]
    print(A)
    print ("\nR1->R1-R2")
    A[0]=A[0]-A[1]
    print (A)
    print ("\nR3->R3-2R3")
    A[2]=A[2]-2*A[1]
    print (A)
    print ("\nR3->-R3/2")
    A[2]=A[2]/(-13)
    print(A)
    print ("\nR1->R1+4R3")
    A[0]=A[0]+4*A[2]
    print (A)
    print("\nR2->R2-5R3")
    A[1]=A[1]-5*A[2]
    print (A)
    print("So x=1;y=4;z=-2")
    
gauss_jordan()

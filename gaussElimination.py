import numpy as np

#The matrix form must be already in [A|b] form
#where A is sistem, and b is the output
def gaussElimination(matrix):
    np.asarray(matrix) #ensure the array
    matrix = matrix.astype(float) #ensure the datatype is float
    print ("the initial matrix:")
    print(matrix)
    if matrix[0,0] == 0.0:
        raise Exception("matrix row 1 column 1 cannot be zero!")
    n,m = matrix.shape
    print ("row:",n,"column:",m)
    #start the elimination phase
    for i in range(0,n):#row
        for j in range(i+1,n):
            if matrix[j,i] != 0.0:
                print ("using row ",i,"as pivot and row ",j,"as target")
                multiplier = matrix[j,i]/matrix[i,i]
                #print matrix[i,k],matrix[k,k],multiplier 
                #just to verbose multiplier process
                matrix[j,i:m]=matrix[j,i:m] - multiplier*matrix[i,i:m] 
                print (matrix)
                
    #start the backsubstitution phase
    x = []
    substractor = 0.0
    for i in range(n-1,-1,-1): #row
        #print "i",i #just for debugging
        for j in range(0,n-i): #column
            #print "j",j #just for debugging
            if j==0:
                substractor = 0
            else:
                substractor = substractor + matrix[i,m-j-1]*x[j-1]
        x.append((matrix[i,m-1]-substractor)/matrix[i,i])
        #print "x",x
    return x
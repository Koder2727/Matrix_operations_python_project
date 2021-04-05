import numpy as np
import matplotlib.pyplot as plt

arr = []
arr_x = []

for n in range (1,1001):
    arr_x.append(n)
    N = n
    
    #make the data points
    divisions = np.linspace(0,1,N+1)
    
    #value of delta
    #it will be distance/N
    Δ = 1/N
    
    #initilize the array with the zeros
    A = np.zeros((N+1,N+1))
    
    #put the values of the boundary
    A[0,0] = 1
    A[N,N] = 1
    
    #due the differential form of boundary condition
    A[N,N-1] = -1

    #make the matrix for the equations
    for i in range(1,N):
        A[i][i] = -2
        A[i][i-1] = 1
        A[i][i+1] = 1
        
    
    #solutions of the x
    B = np.zeros(N+1)
    B[1:-1] = -1*Δ*Δ
    
    #solve the equation
    y = np.linalg.solve(A,B)
    
    #make the analytical matrix
    analytical = divisions - ((divisions)**2)/2
    
    #calculate the numerator error
    error_num = abs(y[1:]-analytical[1:])
    
    #calcualte the denominator error
    error_den = abs(analytical[1:])
    
    #calculate the fianl error and add to the array
    error = (np.sum(error_num/error_den))/(N+1)
    arr.append(error)
    

#plot the array of errors and x
plt.plot(arr_x,arr)
plt.xlabel("Number of Divisions")
plt.ylabel("Error")
plt.show()    
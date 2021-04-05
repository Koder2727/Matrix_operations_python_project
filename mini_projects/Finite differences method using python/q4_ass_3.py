import numpy as np 
from numpy import sin , sinh , pi
import matplotlib.pyplot as plt

#function to calculate the analytic value at particular point at particular n
def V(x,y,i):    
    ans = ((4/(sinh(i*pi) * i * pi)) * (sinh(i*pi*(1-x))) * (sin(i*pi*y)))
        
    return ans

#arrays to store the final error values and points
final_error = []
final_points = []

for N in range(1,100):
    
    #add the point
    final_points.append(N)
    
    #initilize the array with the zeros
    #4 D array will be used 
    #each matrix if the 2d array will represent the solution of the sol(m,n)
    A = np.zeros((N+1,N+1 , N+1,N+1))
    
    #put the values of the boundary eq
    #initialize the value of the coeficient matrix
    for i in range(N+1):
        A[0][i][0][i] = 1
        A[i][0][i][0] = 1
        A[i][N][i][N] = 1
        A[N][i][N][i] = 1
        
    #fill the value of the remaining equations
    for i in range(1,N):
        for j in range(1,N):
            A[i,j,i+1,j] = 1
            A[i,j,i,j+1] = 1
            A[i,j,i,j-1] = 1
            A[i,j,i-1,j] = 1
            A[i,j,i,j] = -4
            
    #the solution matrix will be zero as in question except the boundary condition
    B = np.zeros((N+1,N+1))
    B[0][1:-1] = 1
    
    
    """convert the 4d array into the 2 d array for solving the equation and convert the 
    2d array into the 1 d array""" 
    
    #for A in first row all elements correspondingto the n=0 , next will be n=1 etx
    A = A.reshape(((N+1)**2,(N+1)**2))
    
    #for B the first element corresponds to n=0 and so on
    B = B.reshape(((N+1)**2 ,1))
    
    #solve the obtained 2d equation 
    Sol = np.linalg.solve(A,B)
    Sol = Sol.reshape((N+1,N+1))
    
    #for the calculation of the error
    
    #calculate the error for each point in the equation
    points = np.linspace(0,1,N+1)
    
    #calculate the analytic array
    analytic = np.zeros((N+1,N+1))
    
    #calculate the analiytic value for each corresponding point 
    for i in range(N+1):
        for j in range(N+1):
            for n in range(1,20,2):
                
                #call the function to calculate the value
                analytic[i,j] += V(points[i] , points[j] , n)
    
    
    #calculate the total error in the graph
    total_error = 0            
    for i in range(N+1):
        for j in range(N+1):
            
                ana = analytic[i,j]
                error_num = abs(Sol[i][j] - ana)
                error_den = abs(ana)
                
                #to avoid the zero division error get the value to small number if denominator is zero
                if error_den ==0:
                    error = (error_num/10**(-9))*(1/((N+1)**2))
                else:
                    error = (error_num/error_den)/((N+1)**2)
        
                total_error += error
     
    #add the error into the file
    final_error.append(total_error)

#plotting the error function
plt.plot(final_points,final_error)
plt.xlabel("N")
plt.ylabel("E(N)")
plt.show()
                               

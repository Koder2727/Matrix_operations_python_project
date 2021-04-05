import numpy as np
import matplotlib.pyplot as plt

#specify the number of points
N = 100

#make the data points
divisions = np.linspace(0,1,N+1)

#value of delta will be the difference divided by N
Δ = 1/N

#initilize the array with the zeros
A = np.zeros((N+1,N+1))

#put the values of the boundary
A[0,0] = 1
A[N,N] = 1

#due the differential form of boundary condition
A[N,N-1] = -1

#make the matrix for the equations
#then assign the matrix according to the theroy 
for i in range(1,N):
    A[i][i] = -2
    A[i][i-1] = 1
    A[i][i+1] = 1
    

#solutions of the x at each discraetized point
B = np.zeros(N+1)
B[1:-1] = -1*Δ*Δ

#solve the equation
y = np.linalg.solve(A,B)

#plot the graph
plt.plot(divisions,y)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.show()




                                


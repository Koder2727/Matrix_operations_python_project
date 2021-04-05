import numpy as np
import matplotlib.pyplot as plt


#definig the constants
Np = (10**(21))
q = 1.6 * ((10)**(-19))
e_s = 12*(8.8**(-12))
Lp = 10**(-6)

#specify the number of points

N = 181

#make the data points

divisions = np.linspace(-3*Lp,3*Lp,N+1)

#value of delta
Δ = 6*Lp/N

#initilize the array with the zeros
A = np.zeros((N+1,N+1))

#put the values of the boundary
A[0,0] = 1
A[N,N] = 1

#incorparating the newman boundary condition
A[N,N-1] = -1

#make the matrix for the equations
for i in range(1,N):
    A[i][i] = -2
    A[i][i-1] = 1
    A[i][i+1] = 1
    
print(A)

#solutions of the x
#divide the function into 3 parts 
#<-lp , >lp  , -lp<>lp
p1 = (N+1)//3 
p2 = 2*((N+1)//3) 

#for first and last part the ans is zero
#for he middle division is further divided into 2 parts
p1_1 = (p1+p2)//2

B = np.zeros(N+1)
B[p1:p1_1] = (Np*Δ*Δ*q/e_s)
B[p1_1:p2] = -(Np*Δ*Δ*q/e_s)

#solve the equation
y = np.linalg.solve(A,B)

#plot the graph
plt.plot(divisions,y)
plt.xlabel("X")
plt.ylabel("F(x)")
plt.show()


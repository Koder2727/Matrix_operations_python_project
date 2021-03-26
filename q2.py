import numpy as np        
import sys

arrays = []

with open("C:/Study/SEM 4/Cad/assignment 4/array1.txt") as file:
    array = []
    
    #iterate over each line
    for line in file:
        
        #if the line has no data or empty
        if line.strip() == "":
            
            #append the array to the list of arrays
            arrays.append(array)
            
            #empty array for the next array
            array = []
        
        else:
            
            #append the list to the array
            array.append(list(map(float , line.rstrip().split())))
    
    #append the final list to the list of arrays
    arrays.append(array)

file.close()

a1 = np.array(arrays[0])
a2 = np.array(arrays[1])

sys.stdout = open("array1.txt" , "a")

#addition
print("Addition of a1 and a2\n",a1+a2)
print()

#Multiplication
print("Multiplication of the matrices\n",np.dot(a1,a2))
print()

#Kronecker
print("Kronecker product of the Matrices\n",np.kron(a1,a2))
print()

#Hadmard
print("Hadamard of the Matrices\n",a1*a2)
print()

#Pseudo inverse of a2 and a1
print("Pseudo inverse of the array 1\n",np.linalg.pinv(a1))
print()

print("Pseudo inverse of the array 1\n",np.linalg.pinv(a2))
print()

#determinant
print("Determinant of the matrices\n","a1=",np.linalg.det(a1),"a2=",np.linalg.det(a2))
print()

#rank
print("Rank of the matrices\n","a1=",np.linalg.matrix_rank(a1),"a2=",np.linalg.matrix_rank(a2))
print()

#eigen value of the vectors , the function returns eigen value and eigen vector
e1_a,e_vec_a = np.linalg.eig(a1)
e1_b,e_vec_b = np.linalg.eig(a2)
print("Array of eigen values and eigen vectors of array 1\n" , e1_a ,"\n", e_vec_a)
print("Array of eigen values and eigen vectors of array 2\n" , e1_b ,"\n", e_vec_b)

#Take the pnorm of the matrices by taking the input of the p , use while loop to get the correct input
while True:
    p1 = int(input("Enter the value of p"))
    if(p1>1):
        break
    else:
        print("Wrong input try again")
        
pnorm1 = np.sum(np.abs(a1**p1))**1/p1
print(pnorm1)

while True:
    p2 = int(input("Enter the value of p"))
    if(p2>1):
        break
    else:
        print("Wrong input try again")
        
pnorm2 = np.sum(np.abs(a1**p2))**1/p2
print(pnorm2)

sys.stdout.close()
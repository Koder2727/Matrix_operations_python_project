import numpy as np

#load the matrix from the file 

arrays = []

with open("C:/Study/SEM 4/Cad/assignment 4/array2.txt") as file:
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
v1 = np.array(arrays[1])[0].T

print(a1,v1)

#Find the solution for the given matrix equation
sol = np.linalg.lstsq(a1,v1,rcond=None)

#check if it has no solution
#The linalg.lstsq was not giving error for no solution for some reason so i did like this
if(np.dot(a1,sol[0].T).round(decimals=5) == v1).all():
    print("The solution is : ", sol[0])
else:
    print("No solution")

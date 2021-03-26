import numpy as np
from scipy import linalg , sparse , stats
import sys

from contextlib import redirect_stdout

with open('out.txt', 'w') as f:
    with redirect_stdout(f):

        #Take the rows and coloumns of the matrix
        rows = int(input("Enter the number of rows in the matrix"))
        cols = int(input("Enter the number of cols in the matrix"))
        
        #check if they require identity matrix
        ans = int(input("Do you want indentity matrix?"))
        
        #If the user requires identity , check for the symmetric matrix
        if ans and rows==cols:
            arr=np.identity(rows)
            print(arr)
            sys.exit()
              
        #Take the mean and standard deviaion of the data
        mean = int(input ("Enter the mean of the data"))
        std = int(input("Enter the standard deviation of the data"))
        
        #make an array using the above mea and standard deviation
        arr = np.random.normal(mean,std,(rows,cols))
        
        print(arr)
        #for the symmetric matrix
        if rows == cols:
            matrix_structure = int(input("""Enter the number you want your matrix to be
                                            1.diagonal
                                            2.bidiagonal
                                            3.Block diagonal
                                            4.Symmetric 
                                            5.Skew-symmetric
                                            6.Toepliz
                                            7.Circulant
                                            8.Sparz
                                            9.stochastic
                                            10.Doubly stochastic"""))
        
        #print(arr)
            
            #if the user wants diagonal matrix
            if matrix_structure == 1:
                final = np.diag(np.diag(arr))
                print(final)
            
            #if the user wants bidioginal matrix
            elif matrix_structure ==2:
                
                #get the diagonal and put it in the function to get a diagonal matrix
                diag = np.diag(np.diag(arr))
                
                #get the upper diagonal and put it in the diagonal matrix
                upper_diag = np.diag(np.diag(arr,1),1)
                
                final = diag+upper_diag
                
                print(final)
            
            #if the user wants block diagonal matrix
            elif matrix_structure ==3:
                size = int(input("Enter the size of the blocks"))
                
                #creating the random diagonal for size*size matrix
                diagonal = []
                for i in range(rows):
                    diagonal.append(np.random.normal(mean,std , (size,size)))
                    
                #now create the block diagonal matrix using the above diagonal
                final = linalg.block_diag(*diagonal)
                
                print(final)
            
            #if the user wants symmetric matrix
            elif matrix_structure ==4:
                final = (arr + arr.T)/2
                
                print(final)
            
            #if the user wants skew-symmetric matrix
            elif matrix_structure == 5:
                final = arr - arr.T
                
                print(final)
            
            #if the user wants Toepliz matrix
            elif matrix_structure == 6:
                
                #get all the first coloumn
                col = arr[:][0]
                
                #get the second coloumn
                row = arr[0]
                
                final = linalg.toeplitz(col,row)
                
                print(final)
            
            #if the user wants Circuilant matrix
            elif matrix_structure ==7:
                
                #get the first row in the matrix
                row = arr[0]
                
                final = linalg.circulant(row)
                print(final)
            
            #if the user wants stochastic matrix
            elif matrix_structure == 9:
                
                #divide the rows by their mean 
                for i in range(rows):
                    arr[i] = arr[i]/sum(arr[i])
                    
                print(arr)
            
            #if the user wants stochastic matrix
            elif matrix_structure ==8:
                
                #get the sparsity factor
                sparsity_factor = int(input("Enter the sparsity factor"))
                
                #generate the random variable function
                rvs = stats.norm(mean,std).rvs
                
                final = sparse.random(rows,cols , density = ((sparsity_factor)/(rows*cols)) , data_rvs=rvs)
                
                print(final)
                
            #if the user wants doubly stochastic matrix
            elif matrix_structure == 10:
                
                #keep dividing with avg of row and coloumn sum till both are 1 for all rows and coloumns
                while True:
                    arr = arr/np.sum(arr,0)
                    arr = arr/np.sum(arr,1).reshape(rows,1)
                    
                    if np.all(np.sum(arr,1)==1) and np.all(np.sum(arr,0)==1):
                        break
                
                print(arr)
        
        #For the non symmetric matrix
        else:
            structure = int(input("""Enter the structure of the required matrix
                                      1.stochastic
                                      2.Toepliz
                                      3.sparz"""))
            
            #if the user wants stochastic matrix
            if structure == 1:
                for i in range(rows):
                    arr[i] = arr[i]/sum(arr[i])
                print(arr)
            
            #If the user wants toepliz matrix
            if structure == 2:
                
                #get all the first coloumn
                col = arr[:][0]
                
                #get the first row in the matrix
                row = arr[0]
                
                final = linalg.toeplitz(col,row)
                
                print(final)
            
            #if the user wants sparz matrix
            elif structure == 3:
                sparsity_factor = int(input("Enter the sparsity factor"))
                rvs = stats.norm(mean,std).rvs
                final = sparse.random(rows,cols , density = ((sparsity_factor)/(rows*cols)) , data_rvs=rvs)
                print(final)
                
f.close()           
        

        
    
    
            

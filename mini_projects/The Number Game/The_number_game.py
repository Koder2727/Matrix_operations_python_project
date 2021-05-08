#Program to give the number game
import random
print("Game to guess any number between ")                #asking user to enter the diffucuilty level
while(True):
    print("Select the diffucuilty level")                           
    print("1.Easy(will get 8 chances)") 
    print("2.Medium(will get 6 chanes)")
    print("3.Hard(will get 4 chances)")
    diff=int(input())
    if(diff==1 or diff==2 or diff==3):
        break
    else:
        print("wrong choice, enter again")
        continue
        
num=random.randint(0,20)                                #Generating the required number
print("Enter the number you think machine generated")   #asking user for input

if(diff==1):                                            #running loop for easy diffucuilty
    for i in range(8):                          
        user=int(input())
        if(user==num):
            print("Correct guess, you won")             #Stopping the loop if game is won
            break
        elif(user>num):
            print("Number guessed is greater than original number")#giving user the hint to carry on the game
            if(i!=6):    
                print("Only ",7-i,"more chances remaining")     #kepping track of chances remaining
            else:
                print("last chance remaining")  #giving the final warning to the user
        else:
            print("Number guessed is smaller than original number")
            if(i!=6):    
                print("Only ",7-i,"more chances remaining")
            else:
                print("last chance remaining")
elif(diff==2):
      for i in range(6):
        user=int(input())
        if(user==num):
            print("Correct guess, you won")              #Stopping the loop if game is won
            break
        elif(user>num):                                 #giving user the hint to carry on the game
            print("Number guessed is greater")
            if(i!=4):    
                print("Only ",5-i,"more chances remaining")#kepping track of chances remaining
            else:
                print("last chance remaining")                #giving the final warning to the user
        else:
            print("Number guessed is smaller than original number")
            if(i!=4):    
                print("Only ",5-i,"more chances remaining")
            else:
                print("last chance remaining")
else:
      for i in range(4):
        user=int(input())
        if(user==num):
            print("Correct guess, you won")                  #Stopping the loop if game is won
            break
        elif(user>num):
            print("Number guessed is greater")              #giving user the hint to carry on the game
            if(i!=2):    
                print("Only ",3-i,"more chances remaining")#kepping track of chances remaining
            else:
                print("last chance remaining")                #giving the final warning to the user
        else:
            print("Number guessed is smaller than original number")
            if(i!=2):    
                print("Only ",3-i,"more chances remaining")
            else:
                print("last chance remaining")  
if(user==num):
    print("Congrats you won the game")
else:
    print("Sorry,you lost,better luck next time")                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
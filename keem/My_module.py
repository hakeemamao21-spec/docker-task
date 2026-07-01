#name1 = "SpongeBob"
#name2 = "Pantrick"
#name3 = "Patrick"

#for char1 in name1:
    #for char2 in name2:
        #if char1 == char2:
            #print(char1)
            #break
        #for char3 in name3:
            #if char1 == char3:
                #print(char1)
                #break
        
#x = int(input("please give ma an integer"))
#y = (x*x)*x

#for ans in range(y):
    #if ans** 3 == y:
        #print(ans)
    
X = int(input("please give me a number between 0 and 100: "))
H = 100
L = 0 
guess = (H + L)//2
Num_guess = 1
while (guess != X):
    if (guess > X):
        H = guess
    else:
        L = guess
    guess = (H+L)//2
    Num_guess += 1

print("your guess is ", Num_guess)
print("the number of guesses is ", X)
print("and your final guess is ", guess)
#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that utilizes for loops to provide information and permutations of natural numbers. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defining main function
    ok = True #condition for while loop
    
    while(ok): 
        print("*" * 50) #main menu
        print("                 For Loops Lab")
        print("*" * 50)        
        print("\n1. Display and Add Even numbers from 1 to N")
        print("\n2. Multiplication Table of N") 
        print("\n3. Print Triangle of Numbers")
        print("\n4. Exit\n")
        print("*" * 50) 
        print("")
        
        option = int(input("Choose one of the options to perform: ")) #user input for option
        
        if(option == 1): #option 1
            num = 0
            evenSum = 0
            N = int(input("Enter a natural number for N: "))
            print("Displaying even natural numbers from 1 to 8") 
            for num in range(1, N+1):
                if(num % 2 == 0):
                    print(num)
                    evenSum = evenSum + num
                num = num + 1
            print("")
            print("The sum of even natural numbers from 1 to",N,"is",evenSum)
            print("")
        elif(option == 2): #option 2
            num = 0
            ans = 0
            N = int(input("Enter a natural number for N: "))
            print("Multiplication table of",N)
            for num in range(1, 11):
                ans = N * num
                print(N,"x",num,"=",ans)
                num = num + 1
            print("")
        elif(option == 3): #option 3
            N = int(input("Enter a number of rows to print triangle of numbers: "))
            for num1 in range(1, N+1):
                for num2 in range(1, num1+1): 
                    print(num2, end="") 
                print()
            print("") 
        elif(option == 4): #option 4
            print("Goodbye!")
            ok = False
        else: #option other
            print("Invalid Option!")
            print("Please choose an option between 1 and 4")
            print("")
    
main() #calling main function
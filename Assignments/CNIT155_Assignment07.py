#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that computes using User Defined Functions
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def displayMyInfo(): # displayMyInfo Function
    print("---------------------------------------") 
    print("|          Janith D'Alwis             |") 
    print("|       CNIT 155 Assignment07         |") 
    print("|        jdalwis@purdue.edu           |") 
    print("---------------------------------------")  
    print()

def factorial(N): # factorial Function
    if N < 0:
        return "Factorial not defined for negative numbers"
    elif N == 0:
        return 1
    else:
        num = 1
        for i in range(1, N + 1):
            num *= i
        return num
    
def maximumNo(): # maximum number function
    print("2. Find the Maximum") 
    first_number = int(input("Please enter the 1st number: "))
    second_number = int(input("Please enter the 2nd number: "))
    third_number = int(input("Please enter the 3rd number: "))
    max_number = max(first_number, second_number, third_number)
    print("The greatest number among the three numbers:", max_number)
    return max_number

def digits(N): # digits function
    return len(str(abs(N)))

def main(): # main function
    displayMyInfo() # calling displayMyInfo function
    ok = True 
    while ok: # while loop for menu
        print("==================== User Defined Functions Menu ====================") # user menu 
        print("1. Compute n Factorial") # option 1 
        print("2. Find the Maximum") # option 2
        print("3. Find the number of digits") # option 3 
        print("4. Exit") # option 4 
        print("=====================================================================")
        print()
        
        opt = input("Choose one of the options to perform: ") # user input
        
        if opt == '1': # factorial
            print("1. Compute n Factorial") 
            N = int(input("Enter a natural number for N: "))
            print("Factorial:", factorial(N))
            
        elif opt == '2': # max number finder
            maximumNo()        
            
        elif opt == '3': # num of digit finder
            N = int(input("Enter a number to find its digit count: "))
            print("Number of digits:", digits(N))
            
        elif opt == '4': # exit case
            print("Bye!")
            ok = False
            
        else: # invalid option case
            print("Invalid Option! Enter a number between 1 and 4")
    
main() # calling main function 

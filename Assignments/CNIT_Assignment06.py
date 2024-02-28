#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that uses for loops to provide options for a user to select regarding numbers and graphics. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): 
    opt = True 
    option = ""
    
    while(opt):
        print("\nFor Loops Assignment\n") 
        print("="*40)
        print("\nA. Display Odd natural numbers from N1 to N2, where N2 > N1")
        print("\nB. Find Factorial of N")
        print("\nC. Display Right Angled Triangle of Stars")
        print("\nD. Display Centered Triangle of Stars") 
        print("\nE. Exit")
        
        option = input("\n\nEnter your choice: ") 
        
        if(option == "A"):
            N1 = int(input("\n Enter a natural number for N1: "))
            N2 = int(input(" Enter a natural number for N2: "))
            print("\nDisplaying Odd natural numbers from",N1,"to",N2,"\n")
            for i in range(N1, N2): 
                if(N1 % 2 != 0): 
                    print(N1,"\n")
                N1 = N1 + 1
        elif(option == "B"): 
            N = int(input("\nEnter a natural number for N: "))
            varN = N
            factorial = 1 
            num = 1 
            for num in range (0, N):
                factorial = N * factorial 
                N = N -1
            print("The factorial of",varN,"is:",factorial)
        elif(option == "C"):
            N = int(input("\nEnter number of rows to print *s: "))
            print("Right Angled Triangle of Stars with",N,"rows:")
            num = 0
            for num in range (0, N+1): 
                print("*"*num)
                num = num + 1
        elif(option == "D"): 
            if(option == "D"): 
                N = int(input("\nEnter number of rows to print *s: "))
                print("Centered Triangle of Stars with", N, "rows:\n")
                for i in range(1, N + 1):
                    for space in range(N - i):
                        print(" ", end="")
                    for j in range(2 * i - 1):
                        print("*", end="")
                    print()             
        elif(option == "E"): 
            print("Goodbye!")
            break
        else:
            print("Invalid Input!")
            print("Enter an option between A and E.")

main() 
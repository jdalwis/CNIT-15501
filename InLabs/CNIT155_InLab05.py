#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that displays natural numbers and finds factorials. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
def main(): #defining main function
    options = 0
    while(options != 4):
        print("                         While Loop Lab                                   ") #menu graphic
        print("=================================================================         ")
        print("1. Print all natural numbers between 1 and N.                             ")
        print("2. Display all even natural numbers 1 to N. Compute their sum and average.")
        print("3. Factorial of N                                                         ")
        print("4. Exit                                                                   ")
        print("=================================================================         ")
    
        options = int(input("\n\nChoose one of the following options to perform: ")) #options input
        
        if(options == 1): #Option 1
            N = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers for from 1 to",N)
            num = 1
            while(num <= N):
                print(num)
                num = num + 1
            print("\n")
        elif(options == 2):  # Option 2
            N = int(input("Enter a natural number for N: "))
            print("Displaying even natural numbers from 1 to", N)
            sumEven = 0
            countEven = 0
            for num in range(1, N + 1):
                if(num % 2 == 0):
                    print(num)
                    sumEven = sumEven + num
                    countEven = countEven +1
            if countEven > 0:
                evenAvg = sumEven / countEven
                print("\nThe sum of even numbers from 1 to", N, "is", sumEven)
                print("The average of even numbers from 1 to", N, "is", evenAvg)
            print("\n")        
        elif options == 3: #Option 3
            N = int(input("Enter a natural number for N: "))
            factorial = 1 
            while(N > 0):
                factorial = N * factorial
                N = N - 1  
            print("The factorial is", factorial)
            print("\n")
        elif(options == 4): #Option 4
            print("Goodbye!")  
        else: #Other Option
            print("Invalid Input!") 
            print("Enter a number between 1 and 4.") 
            print("\n")
    
main() #calling main function
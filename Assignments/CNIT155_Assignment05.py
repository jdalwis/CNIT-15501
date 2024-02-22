#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that provides comprehensive information regarding natural numbers. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #importing math library

def main(): #defining main function
    option = "F"
    while(option != "E"): 
        print("*"*55)
        print("                     While Loops")
        print("*"*55)
        print("A. Sum of odd natural numbers from 1 to N")
        print("B. Sum of cubes of odd natural numbers from 1 to N") 
        print("C. Check if a natural number N is a prime number")
        print("D. Print the multiplication table of N")
        print("E. Exit")
        print("*"*55)
        
        option = input("\n\nChoose one of the options to perform: ") #user input for option
        
        if(option == "A"):
            N = int(input("Enter natural number for N: "))
            print("Displaying odd natural numbers from 1 to",N,)
            num = 1
            oddSum = 0
            while(num <= 5):
                if(num % 2 != 0):
                    print(num)
                    oddSum = oddSum + num
                num = num + 1
            print("The sum of odd natural numbers from 1 to",N,"is",oddSum,"\n")
        elif(option =="B"): 
            num = 1
            oddSum = 0
            N = int(input("Enter natural number for N: "))
            print("Displaying the cubes of odd natural numbers from 1 to",N)
            while(num <= N):
                if(num % 2 != 0):
                    print(num**3)
                    oddSum = (num**3) + oddSum
                num = num + 1
            print("The sum of cubes of odd natural numbers from 1 to",N,"is",oddSum)
        elif(option == "C"):
            N = int(input("Enter natural number for N: "))
            if(N > 1 and N % 1 == 0 and N % N == 0): 
                print(N,"is a prime number\n")
        elif(option == "D"): 
            num = 1
            result = 0
            N = int(input("Enter natural number for N: "))
            print("Multiplication table of",N)
            while(num <= 10):
                result = num * N 
                print(N,"x",num,"=",result)
                num = num + 1
            print("\n")
        elif(option == "E"): 
            print("Goodbye!")
        else:
            print("Invalid Input!")
            print("Choose an option between A and E") 
        
main() #calling main function
        
#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Simple and Compound Interest Calculator 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #importing math library

def main(): #defining main function
    print("===============MENU===============\n")
    print("        INTEREST CALCULATOR         ") 
    print("==================================  ")
    print("A. Simple Interest Calculator       ")
    print("B. Compound Interest Calculator     ")
    print("==================================\n")
    
    options = str(input("Choose one of the following options to calculate using the interest: ")) 
    if(options == "A"): #simple interest
        print("You chose option A. Simple Interest Calculator") 
        p = float(input("Enter the principal amount: "))
        t = float(input("Enter the time period in years: ")) 
        r = float(input("Enter the interest rate in percentage %: ")) 
        simpleInterest = (p*(1+((r*t)/100)))
        roundSimpleInterest = round(simpleInterest, 2) #rounding result
        print("The final amount in simple interest is $",roundSimpleInterest) #printing result   
    elif(options == "B"): #compound interest
        print("You chose option B. Compound Interest Calculator")
        p = float(input("Enter the principal amount: "))
        t = float(input("Enter the time period in years: ")) 
        r = float(input("Enter the interest rate in percentage %: "))
        n = float(input("Enter the number of terms per year: ")) 
        compoundInterest = p*math.pow(1+(r/(100*n)), n*t)
        roundCompoundInterest = round(compoundInterest, 2)
        print("The final amount in compound interest is $", roundCompoundInterest)
    else: #other
        print("Invalid input!\nPlease enter your choice either A or B.") 
       
main() #calling main function
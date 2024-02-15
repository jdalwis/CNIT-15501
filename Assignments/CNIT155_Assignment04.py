#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Quadratics Program that prints equation, discriminant, and roots. 
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #importing math library

def main(): #defining main function
    print("        ++++++++++++++++++++++++++++++++++++++  ") #introduction
    print("        +                Janith              +  ")
    print("        +          jdalwis@purdue.edu        +  ") 
    print("        +        CNIT 155 Assignment 04      +  ") 
    print("        ++++++++++++++++++++++++++++++++++++++\n")
    
    print("Second Degree quadratic equation roots calculator: aX^2 + bX + c = 0\n") 
    a = input("        Enter the coefficient a: ") #user input for coefficients
    b = input("        Enter the coefficient b: ")
    c = input("        Enter the coefficient c: ")
    quadEquation = a+"X^2 + "+b+"X"+" + "+c +" = 0"
    print("\n        Quadratic Equation is:", quadEquation)
    varA = float(a) #type casting the variables as floats.
    varB = float(b)
    varC = float(c)
    discrim = ((math.pow(varB,2) - (4*varA*varC)))
    roundDiscrim = round(discrim, 3)
    print("\n        The Discriminant is:", roundDiscrim)
    
    print("\nCalculating the roots..................\n")
    
    if discrim < 0: #if statement for roots
        print("        The equation has no real roots.")
    elif discrim == 0: 
        root1 = round((-varB + math.sqrt(discrim)) / (2*varA), 3)          
        print("        The equation has one real root:", root1)
    else: 
        root1 = round((-varB + math.sqrt(discrim)) / (2*varA), 3)
        root2 = round((-varB - math.sqrt(discrim)) / (2*varA), 3)         
        print("        The equation has two real roots:", root1, "and", root2) 
    
    if varA < varB and varA < varC: #if statement for smallest coefficient 
        smallCoefficient = varA
    elif varB < varA and varB < varC: 
        smallCoefficient = varB
    else:
        smallCoefficient = varC
    print("\n        The smallest coefficient is:", smallCoefficient)
    
main() #calling main function

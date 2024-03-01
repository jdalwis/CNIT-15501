#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that determines validity of triangles. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#================================================================= 

def displayMyInfo(): # function to display header
    print("       *****************************")
    print("       *       Janith D'Alwis      *")
    print("       *     jdalwis@purdue.edu    *")
    print("       *      CNIT155 InLab07      *")
    print("       *****************************")

displayMyInfo() # calling displayMyInfo functions
        
def validate(A,B,C): # function to validate triangle
    if A+B > C:
        return True
    else: 
        return False
    
def computePerimeter(A,B,C): # function to compute Perimeter
    perimeter = round((A + B + C),2)
    return perimeter
    
def main(): # defining main function
    opt = True
    while opt == True: #option loop 
        A = float(input("Enter the length of side a of a triangle: ")) # user input for side A
        B = float(input("Enter the length of side b of a triangle: ")) # user input for side B
        C = float(input("Enter the length of side c of a triangle: ")) # user input for side C
        
        print("\nValidating a triangle...\n")  
        
        if validate(A,B,C) == True: # calls validate function
            print("This is a valid triangle")
            repeat = True
            print("The perimeter of the triangle is",computePerimeter(A,B,C),"\n") # calls computePerimeter function
        elif validate(A,B,C) == False: # calls validate function
            print("Inputs can not form a triangle. Please enter different numbers!\n")
            repeat = False
        
        while repeat == True: # loop to repeat program
            userOpt = str.upper(input("Do you want to compute again? (Y/n): "))    
            if userOpt == "Y":
                main()
            elif userOpt == "N":
                print("End of the Program") 
                exit() # exits program
            else: # invalid input condition
                print("Invalid Input")
                print("Press Y or N, case insensitive:")
                repeat == True 
            
    
main() # calls main function
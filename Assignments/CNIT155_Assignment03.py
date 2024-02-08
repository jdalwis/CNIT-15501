#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that calculates the side area, bottom area, and volume. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================
import math #imported math library  

def main(): #defining main function
    varD1 = float(input("Enter a value for Depth1 (D1): ")) #user input
    varD2 = float(input("Enter a value for Depth2 (D2): "))
    
    if (varD2 < varD1): #if statement condition 
        print("Invalid input! D2 must be greater than D1!") #invalid input message
        return #function returns if D1 > D2
    
    varW = float(input("Enter a value for Width (W): "))
    varL = float(input("Enter a value for Length (L): "))
    print("\n")
    
    varSideArea = (varD1 + varD2) * (varL/2) #Side Area 
    varD3 = (varD2 - varD1) #Depth 3
    varHyp = (math.sqrt((varD3**2)+(varL**2))) #Hypotenuse 
    varBottomArea = (varHyp * varW) #Bottom Area
    varRoundBottomArea = round(varBottomArea, 2) #Bottom Area Rounded
    varVolumePool = (varSideArea * varW) #Volume of Pool
    
    print("Calculating....\n") #calculating message
    
    print("The side area of the pool is:", varSideArea)
    print("The bottom area of the pool is:", varRoundBottomArea)
    print("The volume of the pool is:", varVolumePool) 

main()
    
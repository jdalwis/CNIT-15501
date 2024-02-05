#===============================================================
# Your Name & Lab Section: Janith D'Alwis 
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Finding the volume, lateral area, and surface area of a truncated cone. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified
# I have not given other fellow student(s) access to my program.
#=================================================================
import math

def main(): 
    print("          Properties of a Truncated Cone") 
    print("          -------------------------------") 
    r1 = float(input("Enter radius 1 (r1) of a cone: "))  
    height = float(input("Enter the height of a cone: ")) 
    slantHeight = float(input("Enter the slant height of a cone: ")) 
    r2 = float(input("Enter radius 2 (r2) of a cone: "))
    volume = (1/3)*(math.pi)*height*((r1**2)+(r1*r2)+(r2**2))
    latArea = (slantHeight*(math.pi)*(r1+r2))
    surArea = (latArea + (math.pi*((r1**2)+(r2**2))))
    roundVolume = round(volume, 2) 
    roundLatArea = round(latArea, 2)
    roundSurArea = round(surArea, 2) 
    line = "_"
    print(line*100, "\n") 
    print("Calculating..\n") 
    print("The volume of the truncated cone is:",roundVolume) 
    print("The lateral area of the truncated cone is:",roundLatArea) 
    print("The surface area of the truncated cone is:",roundSurArea) 
    
main()
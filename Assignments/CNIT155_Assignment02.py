#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: In your own words, provide a brief, meaningful
# description of the program in 1-2 sentences (just “Assignment02” is not meaningful).
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defined the main function
    #intro graphic
    print("*" * 50) #multiplying a string to create a line graphic
    print("*              CNIT155 Assignment 02             *") 
    print("*") 
    print("*              Conversion Calculator             *")
    print("*" * 50, "\n") #\n to create a blank line
    
    #printing name 
    varName = input("Enter your full name: ")
    print("My name is", varName, "\n")
    
    #pounds to kg conversion
    print("** 1st. Pounds to Kilograms Conversion **") 
    varPounds = float(input("What is the weight in pounds to convert it to kilograms?: ")) 
    varKilograms = (varPounds*0.45359237)
    varRoundKilograms = round(varKilograms, 2) 
    print("The weight entered in pounds is", float(varPounds)), "and it is", varRoundKilograms, "kg\n")
    
    #celsius to fahrenheit conversion
    print("** 2nd. Celsius to Fahrenheit Conversion **") 
    varCelsius = float(input("Enter the Celsius temperature to convert it to Fahrenheit: "))
    varFahrenheit = (varCelsius*(9/5)+32)
    varRoundFahreneheit = round(varFahrenheit, 2) 
    print("The entered temperature in Celsius is", varCelsius, "C and it is", varRoundFahreneheit, "F\n")
    
    #miles to kilometers conversion
    print("** 3rd. Miles to Kilometers Conversion **")
    varMiles = float(input("Enter miles to convert it to kilometers: ")) 
    varKilometers = (varMiles*1.60934)
    varRoundKilometers = round(varKilometers, 2)
    print("The entered distance in miles is", varMiles, "mi and it is", varRoundKilometers, "km\n")
    
    #yards to meters conversion
    print("** 4th. Yards to Meters Conversion **") 
    varYards = float(input("Enter yards to convert it to kilometers: "))
    varMeters = (varYards*0.9144)
    varRoundMeters = round(varMeters, 2) 
    print("The entered distance in yards is", varYards, "yards and it is", varRoundMeters, "m\n")
    
    #feet and inches to centimeters 
    print("** 5th. Feet and Inches to Centimeters **") 
    varFeet = float(input("Feet: ")) 
    varInches = float(input("Inches: "))
    varTotalInches = ((varFeet*12)+varInches)
    varCentimeters = float(varTotalInches*2.54)
    varRoundCentimeters = round(varCentimeters, 2) 
    print("The entered height is", int(varFeet), "feet", int(varInches), "inches and it is", varRoundCentimeters, "cm")
   
main() #called main function
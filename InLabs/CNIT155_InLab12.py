#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Provides information regarding steps taken to the user. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def stepsToMiles(lst): # defining main function 
    miles_strings = []
    total_miles = 0
    for day, steps in enumerate(lst, start=1): # iterating through steps, starting point  
        miles = steps / 2000
        total_miles += miles
        miles_strings.append(f"Day {day}: {miles:.2f} miles")
    avg_miles = total_miles / len(lst)
    return '\n'.join(miles_strings), avg_miles # returning days and miles joined togethers

def main(): # defining main function 
    print("*******************************************************") # printing header 
    print("**********                                   **********")
    print("**********     Steps to Miles Calculator     **********")
    print("**********                                   **********")
    print("*******************************************************\n")
    
    count = 1
    lst = []
    
    while len(lst) < 7: 
        try: 
            steps = int(input(f"Enter the number of steps for Day {count}: ")) 
    
            if(steps > 0): 
                count += 1 
                lst.append(steps) # appending user input 
            else: 
                raise ValueError # raising ValueError
                
        except ValueError: # ValueError exception 
            print("\nException: Wrong Value Entered") 
            print("Please enter an integer value in a correct format!\n") 
    
    miles_info, avg_miles = stepsToMiles(lst)
    
    print("\n*** The number of miles you walked this week ***")
    print(miles_info)
    
    print(f"\nThe average miles walked per day: {avg_miles:.2f} miles")
    
    print("\nEnd of the program") # end of program statement 
    
main() # calling main function 

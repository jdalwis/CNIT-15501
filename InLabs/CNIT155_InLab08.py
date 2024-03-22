#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that computes GPA averages 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): # defining main function
    names = [] # initializing names list
    gpaList = [] # initializing gpa List
    sum = 0 
    avgGpa = 0
    
    count = int(input("How many students are there in your class?: ")) # num of students input
    
    for i in range (1, count+1): 
        name = str(input(f"Input student #{i} name: "))
        names.append(name) # appending to names list
        while True: 
            gpa = float(input(f"Input student #{i} gpa: ")) 
            if gpa >= 0 and gpa <= 4.0: # regular gpa case
                break
            else: 
                print("A GPA must be between 0 and 4.0 (both inclusive)!\n") # irregular gpa case
        gpaList.append(gpa) # appending to gpa list
        
    print("============== List ==============") 
    print("     Name                GPA      ")
    print("  ----------          ----------  ")
    for j in range(len(gpaList)):
        print("    ",names[j], "\t\t", gpaList[j])
        sum = sum + gpaList[j]
        
    for k in range(0, len(gpaList)): # avg gpa functions
        avgGpa = avgGpa + gpaList[k]
        
    finalAvgGpa = avgGpa/len(gpaList)
    maxGPA = max(gpaList) # max gpa
    minGPA = min(gpaList) # min gpa 
        
    print("\n=================================================")
    print("The average of entered GPAs is",'{0:.2f}'.format(finalAvgGpa))
    print("The maximum GPA is",'{0:.2f}'.format(maxGPA))
    print("The minimum GPA is",'{0:.2f}'.format(minGPA))
    print("=================================================")
    
    
main() # calling main function
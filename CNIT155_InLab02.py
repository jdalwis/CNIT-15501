#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that prints out information regarding number of students, price of a textbook, today's temp, and a car trip.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): #defining main function
    #introduction
    print("This is InLab02 for CNIT155 by Janith D'Alwis\n")
    
    #number of students
    studentnum = int(input("Enter the number of students in CNIT 155: "))
    print("The number of students in CNIT 155 is:",studentnum)
    print("The data type of the number of students is:",type(studentnum),"\n")
    
    #price of textbook
    textbookprice = float(input("Enter the price of the textbook: "))
    textbookpriceround = round(textbookprice, 2) 
    print("The price of the textbook is: $", textbookpriceround)
    print("The data type of the price of the textbook is:",type(textbookpriceround),"\n")
    
    #today's temperature
    todaytemp = float(input("Enter today's temperature in Fahrenheit (°F): "))
    celciustemp = (todaytemp - 32)*5/9
    celciustempround = round(celciustemp, 2)
    print("Today's temperature in Celcius is:",celciustempround)
    print("The data type of the temperature is:",type(celciustempround),"\n")    
    
    #distance travelled 
    distancetraveled = float(input("Enter the distance traveled by the car in miles: "))
    timetraveled = float(input("Enter the duration of the trip in hours: "))
    print("The number of students in CNIT 155 is:",studentnum)
    speed = float(distancetraveled/timetraveled)
    speedround = round(speed, 2) 
    print("The average speed of the car for the trip is:", speedround,"miles/hour")
    print("The data type of speed is:",type(studentnum),"\n")    
    
main() #calling main function
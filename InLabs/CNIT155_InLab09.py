#================================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that converts USD to Yuan and provides additional information re currency. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified. 
# I have not given other fellow student(s) access to my program.
#=================================================================

def UsdToYuan(lst): # defining UsdToYuan function
    yuanlst = []
    for cost in lst: # for loop that iterates through USD and converts to Yuan
        yuancost = cost * 7.21
        yuanlst.append(yuancost) 
    return yuanlst # returning yuanLst
    
def PrintInfo(lst1, lst2): # defining PrintInfo function 
    print("")
    print("         USD($)                          Yuan(¥)          ")
    print("#############################################################")
    for i in range(len(lst1)): 
        print(f"{lst1[i]:>13.2f}                     {lst2[i]:>10.2f}")
    print("#############################################################")

def Average(lst): # defining Average function
    return sum(lst) / len(lst)

def FindPrice(lst1, lst2): # defining FindPrice function
    print("################# Price(s) under $70 is(are) #################")
    print("        USD($)                       Yuan(¥)              ")
    print("       --------                      -------              ")
    for i in range(len(lst1)): 
        if lst1[i] < 70: 
            print(f"{lst1[i]:>13.2f}                     {lst2[i]:>10.2f}")

def main(): # defining main function 
    USD = [] # initializing USD list
    Yuan = [] # initializing Yuan list 
    
    while True: 
        price = input("Enter a price in USD. Use NN or nn to stop data entry: ") # user input for USD 
        if price.lower() == 'nn': # breaking if user inputs nn or NN
            break
        else: 
            USD.append(float(price)) # appending to USD list
    print("Number of prices entered: ",len(USD))
    
    Yuan = UsdToYuan(USD) # assigning UsdToYuan function to Yuan variable 
    
    PrintInfo(USD, Yuan) # calling PrintInfo Function
    
    print("")
    print("###################### Averages ########################")
    print(f"The average of the prices is USD {Average(USD):.2f}")
    print(f"The average of the prices is Yuan {Average(Yuan):.2f}")
    
    print("")
    FindPrice(USD, Yuan) # calling FindPrice function
    
main() # calling main function 

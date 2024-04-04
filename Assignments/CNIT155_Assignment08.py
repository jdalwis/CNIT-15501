#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program for items in a store that performs functions. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def Discount(lst): # defining Discount functions
    discountPrices = [9.09, 57.74, 82.52, 125.29, 40.24, 139.99] # updated prices 
    lst.clear() # clearing lst
    lst.extend(discountPrices)
    return lst # returning lst

def PrintInfo(lst1, lst2, lst3): # defining PrintInfo function
    print("     Name                ID          Price") 
    print("====================================================")
    for i in range(len(lst1)): 
        print(f"     {lst1[i]:<15}   {lst2[i]:<10}   {lst3[i]:<10.2f}")
    print("")

def Average(lst): # defining Average function
    return round(sum(lst)/len(lst),2) # returning rounded lst 

def Search(lst1, lst2, lst3, avg): # defining Search function 
    print("     Name                ID          Price") 
    print("====================================================")
    for i in range(len(lst1)):
        if lst3[i] <= avg:
            print(f"     {lst1[i]:<15}   {lst2[i]:<10}   {lst3[i]:<10.2f}")
    print("")
        
    
def main(): # defining main function 
    Names = ["Paint Brush", "Sander", "Hand Drill", "Vac Cleaner", "Roller", "Chainsaw"] # Names list
    IDs = [3750, 4389, 3986, 9562, 1967, 2988]                                           # IDs list
    Prices = [12.99, 82.49, 117.89, 178.99, 57.49, 199.99]                               # Prices List
    Updated = []                                                                         # Updated List
    
    print("****************************************************") # printing main header 
    print("**********         Assignment 08          **********")
    print("****************************************************")
    
    PrintInfo(Names, IDs, Prices) # printing Info
    
    print("****************************************************") # printing averages header 
    print("=================     Averages     =================")      
    print("The average of prices before the discount is $",Average(Prices))
    
    print("")
    print("****************************************************")
    print("Prices have been adjusted!")
    
    Discount(Updated) # applying discount to make Updated List
    PrintInfo(Names, IDs, Updated) # printing Info
    
    print("****************************************************") # printing updated averages headers
    print("=================     Averages     =================")    
    print("The average of prices after the discount is $",Average(Updated))
    
    print("")
    print("================ Products <= $",Average(Updated),"===============")
    
    Search(Names, IDs, Updated, Average(Updated)) # Using the search function to generate products below average price
    
main() # calling main function 
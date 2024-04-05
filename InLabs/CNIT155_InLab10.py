#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that reads and writes to a text file. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#================================================================

def main(): # defining main function 
    try: 
        # open two files
        inputFile = open("scores.txt", "r")
        outputFile = open("scores_stat.txt", "w")
        
        # reads the contents of the input file and stores into scores variable
        scores = inputFile.readlines()
        
        # use sublist to remove the first three non-numeric elements 
        scores = scores[3:]
        
        # Converts scores values into float datatypes 
        scores = [float(score.strip()) for score in scores] 
                  
        # prints contents of scores.txt file
        print("Printing the contents of the file...") 
        print("")
        print(scores)
        
        # Calculate max, min, sum, avg, and num of scores 
        max_score = max(scores)
        min_score = min(scores)
        sum_scores = sum(scores)
        avg_score = round(sum_scores / len(scores),2) 
        num_scores = len(scores) 
        
        # Writes the output of these calculations to scores_stats.txt file 
        outputFile.write(f"The number of scores in the list is {num_scores}\n")
        outputFile.write(f"The average of scores in the list is {avg_score}\n")
        outputFile.write(f"The maximum score is {max_score}\n")
        outputFile.write(f"The minimum score is {min_score}\n")
        
        inputFile.close()
        outputFile.close()
        
    except FileNotFoundError: # exception 
        print("The program failed to open the file. Make sure of the following:") 
        print("        The file to read is located in the same folder where this program is.")
        print("        The file's name is spelled correctly.")

main() # calling main function 
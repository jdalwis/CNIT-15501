#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that returns book analysis. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main(): # defining main function 
    try:
        inputFile = open("books1.txt", "r") # opening input file
        outputFile = open("books_analysis.txt", "w") # creating output file       
        books = inputFile.readlines() # reading input file 
        bookCount = len(books) # finding length of input file 
            
        print("Printing the contents of the file...\n")
        print(books, "\n") # printing books 
            
        outputFile.write("======= Analysis Results =======\n\n") # header 
        outputFile.write(f"1. The number of books in the file: {bookCount}\n\n") # printing book count 
        outputFile.write("2. Titles of Books which have more than 2 words:\n\n")
            
        for title in books: # books with more than two words
            title = title.strip() # removes white space
            if len(title.split()) > 2: # checks if there is more than two words 
                outputFile.write(title + "\n") # writes to output file 
            
        outputFile.write("\n3. Organized Book Titles:\n\n")
        for title in sorted(books): # books with title function applied 
            title = title.strip().title() # removes white space and applies title function 
            outputFile.write(title + "\n") # writes to output file 
            
        inputFile.close() # closes input file 
        outputFile.close() # closes output file         

    except FileNotFoundError: # exception case 
        print("The program failed to open the file. Make sure of the following:")
        print("        The file to read is located in the same folder where this program is.")
        print("        The file's name is spelled correctly.")


main() # calling main function 

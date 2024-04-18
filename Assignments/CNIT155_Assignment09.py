#===============================================================
# Your Name & Lab Section: Janith D'Alwis, Friday 1:30pm
# Your Purdue Email: jdalwis@purdue.edu
# Program Description: Program that conducts statistical analysis on Students and their GPAs. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program.
#=================================================================

def main():  # defining main function
    try:
        inputFile = open("input.txt", "r")
        outputFile = open("output.txt", "w")

        file = inputFile.readlines()

        Names = []
        Scores = []

        for line in file:
            cleanLine = line.strip()
            Temp = cleanLine.rsplit(" ", 1)
            namePart = Temp[0].title()
            Names.append(namePart)
            Scores.append(float(Temp[1]))
            
        print("Printing all content in the file...") 
        print(Names)
        print(Scores) 
        print("Scores have been updated...") 

        # Update scores by adding 0.1, making sure not to exceed 4.0
        UpdatedScores = [min(score + 0.1, 4.0) for score in Scores]

        # Convert scores to letter grades based on the provided scale
        def score_to_grade(score):
            if score >= 3.7:
                return 'A'
            elif score >= 3.5:
                return 'B'
            elif score >= 3.0:
                return 'C'
            elif score >= 2.5:
                return 'D'
            else:
                return 'F'

        Grades = [score_to_grade(score) for score in UpdatedScores]

        # Find the maximum score after the update
        maxScore = max(UpdatedScores)
        outputFile.write("Maximum score is: {:.1f}\n".format(maxScore))

        # Write the names with the maximum score
        for name, score in zip(Names, UpdatedScores):
            if score == maxScore:
                outputFile.write("{}, {:.1f}\n".format(name, score))

        outputFile.write("\nUpdated score(s) with letter grade:\n")

        # Write all names, updated scores, and letter grades
        for name, score, grade in zip(Names, UpdatedScores, Grades):
            outputFile.write("{}, {:.2f}, {}\n".format(name, score, grade))

        # Close the files
        inputFile.close()
        outputFile.close()

    except FileNotFoundError:  # exception for file not found
        print("The program failed to open the file. Make sure of the following:")
        print("        The file to read is located in the same folder where this program is.")
        print("        The file's name is spelled correctly!")


main()  # calling main function

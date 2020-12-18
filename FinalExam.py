"""
The program will calculate and display the number of grades, the average grade, and the percentage of grades that are 
above the average grade to the user.  First we define a main function
under this main function we open the final.txt file  and assign integers to each score. 
After we have the number of scores in the txt document 
we must close the txt file. After we have all the scores read into the memory, 
we take the sum of all the scores that were in the txt file and add them up, after this we 
divide the sum by the amount of scores in the txt file in order to find the average grade. 
After we calculate the average grade, we take the scores above the average grade and divide them by the amount of 
scores that were in the finals.txt file and multiply it by 100 in order to find the percentage of scores
that were above the average grade. 
The correct answers should be as follows:
Number of grades: 24
Average grade: 83.25
Percentage of grades above average: 54.17 
"""


"""
main ():
  set grades = input
  calculate average = Cal_ave
  calculate above average grades = above_ave

grades():
open (finals.txt)
set finals equal to integers
close finals.txt
print "There are", grade, "in this class"

cal_ave():
add together all grades = sum1
average = sum1/grade

above_ave():
if grade > ave_grade
count
if not
do not ocunt
count all grades above ave_grade
above_ave = amount of above_ave_grade/ave_grades * 100

main()
"""

def main():

def AmtofGrades():
  infile = open (final.txt, "r")
  grades = line.rstrip() for line in infile
  for i in range (len(grades)):
  print ("The number of grades is:" AmtofGrades)

def calculate_percentage_above_grades():
  percentAboveAverage = countif grades > ave_grade
    percentAboveAverage/ AmtofGrades * 100
    print ("The percentage of the grades that were above average is:", calculate_percentage_above_grades)


def averageGrade():
ave_grade = sum (final.txt) / AmtofGrades
  print ("The average grade in the class is:" averageGrade

main()
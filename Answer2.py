
## Question 1: 
#The user will be asked for their First Name, Last Name, Student Number, names of 4 courses, and the Midterm and Final grades for these courses. The year-end average will be calculated by adding 40% of the Midterm grade to 60% of the Final grade. If the average is below 50, "FAILED" will be displayed on the screen; if it is 50 or above, "PASSED" will be displayed. This printing process will be done for all 4 courses and the courses will be listed one below the other.
    
first_name = input("Please enter your name: ")
last_name = input("Please enter your last name:" )
student_nr = int(input("Please enter your student number: "))
name_of_course1 = input("Please enter your first course: ")
name_of_course2 = input("Please enter your second course: ")
name_of_course3 = input("Please enter your third course: ")
name_of_course4 = input("Please enter your fourth course: ")
the_midterm =  int(input("Please enter your the midterm grades: "))
final_grades =  int(input("Please enter your the final grades: "))
avarage = the_midterm*0.40 + final_grades*0.60

if avarage < 50:
    print("FAILED")
elif avarage >= 50:
    print("PASSED")


## Question 2: 
#Write a Python program that calculates the average of the numbers in the list below. Then, add a "for" loop that separates each number in the list into "high" if it is greater than the average, and "low" if it is lower than the average, and print the count of each group on the screen.

numbers = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
the_average = sum(numbers)/len(numbers)

for x in numbers:
    if x <= 10:
        print(x)
    if x > 10:
        print(x)
    

## Question 3: 
#Write a Python program that calculates the sum of odd numbers in a given range. The program will ask the user for two numbers and calculate the sum of odd numbers between these two numbers. The program will print an error message if the user makes an invalid entry. You must use a While loop in writing the program.

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
sum = number1 - number2
x = sum
while x < -111:
    print(x)
    x -= 10
    





 



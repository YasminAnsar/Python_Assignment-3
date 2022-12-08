##########################################################################################################
#### Question-#1
##########################################################################################################
# Write a program that reads an integer from the user. Then your program should 
# display a message indicating whether the integer is even or odd and if the number
#  is a prime or a non-prime.
number = int(input("Enter the number: "))

if (number%2 == 0 and number == 2):
    print(f"{number} is even and prime number")
elif(number%2 == 0):
    print(f"{number} is even and Non-prime number")
elif (number%2 != 0):
    for i in range(2, number):   # it will devide number for all the factors in range 
        if number % i == 0:
            print(f"{number} is odd and a Non-prime number")
            break
    else:
        print(f"{number} is odd and a prime number")
##########################################################################################################
#### Question-#2
##########################################################################################################
#Write a program that computes the real roots of a quadratic function. Your program
#should begin by prompting the user for the values of a, b and c. Then it should display
#a message indicating the number of real roots, along with the values of the real roots
#(if any).
import math
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
# Part of formula for calculating root 
d = b**2 - 4*a*c
# Conditions for calculating roots and printing the outputs
if d > 0:
    root1 = (-b + math.sqrt(d))/2*a
    root2 = (-b - math.sqrt(d))/2*a
    print("Root1 = %.2f; Root2 = %.2f" %(root1, root2))
elif d == 0:
    root1 = -b/2*a
    print("Root1 %.2f" %(root1))
else:
    print("It has no roots")

##########################################################################################################
#### Question-#3
##########################################################################################################
#In this exercise, you will create a program that computes the average of a collection
#of values entered by the user. The user will enter 0 as a sentinel value to indicate
#that no further values will be provided. Your program should display an appropriate
#error message if the first value entered by the user is 0.

#Defining a function for calculating average
def avg(mycollection):
    average = 0 if len(mycollection) == 0 else round((sum(mycollection)/len(mycollection)), 2) 
    return (f"Average of the given numbers is {average}")
#An empty list that will hold values from user
mycollection = []
user_input = int(input("Enter the value and 0 to exit: "))
if (user_input == 0):
    print("Sorry wrong start: Try again with number other than '0'")
else:
    while (user_input != 0):
        mycollection.append(user_input)
        user_input = int(input("Enter the value and 0 to exit: "))
print(avg(mycollection))
##########################################################################################################
#### Question-#4
##########################################################################################################

#Write a program that displays a temperature conversion table for degrees Celsius and
#degrees Fahrenheit. The table should include rows for all temperatures between 0
#and 100 degrees Celsius which are multiples of 10 degrees Celsius. Include appropriate
#headings on your columns. The formula for converting between degrees Celsius and
#degrees Fahrenheit can be found on the internet.
import numpy as np
import pandas as pd
def c_to_f(Celcius):
    fahrenheit = round(float((Celcius * 9/5) + 32))
    return fahrenheit
#initialize list of values ranging from 0 through 100 multiple of 10
celcius_list = np.arange(0,110,10)    #np.arrange(start,stop,step) creates an array by taking start,stop and step values
fahrenheit = []                       #Creating empty list for Fahrenheit values
for i in range(len(celcius_list)):    #adding values to farhenheit list through c_to_f()
    fahrenheit.append(c_to_f(celcius_list[i]))
#Create DataFrame with column names "Celcius" and   "Fahrenheit"
df = pd.DataFrame({'Celcius': celcius_list,'Fahrenheit': fahrenheit})
#prit dataframe
print(df)


##########################################################################################################
#### Question-#5
##########################################################################################################
group_ages = []
charge = 0
age = int(input("Please enter your age and if want to exit then enter -1: "))
while age != -1:
    group_ages.append(age)
    if age > 0  and age <= 2:
        charge += 0
    elif age >= 3 and age <= 12:
        charge += 14.00
    elif age >= 65:
        charge += 18.00
    else:
        charge += 23.00
    age = int(input("Please enter your ageand if want to exit then enter -1: "))
print(f"Your have to pay for the ages {group_ages} to enter in the zoo is ${charge}")

##########################################################################################################
#### Question-#6
##########################################################################################################

import math
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))

def hypotenuse_calc(side1,side2):
    hypotenuse = round(math.sqrt(side1**2 + side2**2),2)
    return (f"The hypotenue of the right trianl=gle of sides {side1} and {side2} are {hypotenuse}")
hypotenuse_calc(side1,side2)

##########################################################################################################
#### Question-#7
#####################################################################################################
#An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item, and $2.95 for each subsequent item. Write a function that takes the
# number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result. Include user inputs that read the number of
# items purchased from the user and display the shipping charge.

#Taking user input for number of items
items = int(input("Please enter the number of items in your order: "))
#Function for calculating shipping charge 
def charge_calc(items):
   fixed_charge = 10.95
   subsequent_charge = 2.95
   result  = round(fixed_charge + (items-1)*subsequent_charge,2)
   print(f" The shipping charges for {items} items are ${result}")
#Calling the function
charge_calc(items)


##########################################################################################################
#### Question-#8
#####################################################################################################

#Declaring a password check funtion to check if its meeting the desire requiremnts or not

def password_check(password):
    #Declaring variable and setting them to False 
    psw_length = False
    psw_lower = False
    psw_upper = False
    psw_digit = False
    #If stament to chekc if length of password is desired length
    if len(password) >= 8:
        psw_length = True
    #For loop to check if any one of the charter is uppercase , lowercase,and a digit
    for i in password:
        if i.islower():
            psw_lower = True
        elif i.isupper():
            psw_upper = True
        elif i.isdigit():
            psw_digit = True
    #If stament that checks if all the variable are true then it will retirn true otherwise it will return false
    if (psw_length == True and psw_lower == True and psw_upper == True and psw_digit == True):
        return True
    else: 
        return False

#Definging a main function that will call this passweord_check function
def main():
    password = input("Please enter the password: ")
    if password_check(password):
        return ("It is a strong password")
    else:
        return ("It is a weak password")

#Calling the main funtion
main()

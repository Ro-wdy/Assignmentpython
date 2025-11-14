#try, except, else(optional), finally(optional)
#Exception handling for a number when divided by zero

from dbm import error
from operator import add


try:
 x = int(input("input your first number: "))
 y = int(input("input your second number: "))
 result = x / y
 print(result)
    
except ZeroDivisionError:
 #when the division by zero is typed
 print("Error: Division by zero is not allowed.")
 
 #when a user inputs something far from a number
except ValueError:
 print("Error: Invalid input. Please enter numeric values only.")

else:
 print(f"The numbers {x} and {y} were divided successfully.")


try:
 a = input("enter you number")
 b= input("enter second number")
 result=int(a)/int(b)

 print (result)

except ZeroDivisionError as A:
 print (A)

finally:
 print("success ")


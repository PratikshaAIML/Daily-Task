#Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 
 

  def div(a, b): 

    if b == 0: 

        return "Cannot divide by zero" 

    return a / b 

 

# Calling the function with two numbers 

result = div(10, 2) 

 

# Displaying the result 

print("The result of the division is:", result) 



 
 
##############################################################################################################################

Declare a square() function with one parameter.Then call the function and pass one 

number and display the square of that number . 
def square(number): 

    return number * number 

 

# Calling the function and passing a number 

result = square(5) 


# Display the result 

print("The square of 5 is:", result) 



 
##############################################################################################################################
 

#Using max() and min() functions display the maximum and minimum of 5 random numbers. 

# List of 5 random numbers 

numbers = [23, 45, 12, 78, 34] 
# Using max() to find the maximum number 
maximum = max(numbers) 

# Using min() to find the minimum number 
minimum = min(numbers) 

  
# Displaying the results 

print("The maximum number is:", maximum) 

print("The minimum number is:", minimum) 

 


##############################################################################################################################
 

#Accept a name from the user and display that in lower case using lower() function 

# Accepting a name from the user 

name = input("Enter your name: ") 

# Converting the name to lowercase using lower() 

lowercase_name = name.lower() 

# Displaying the name in lowercase 

print("Your name in lowercase is:", lowercase_name) 


 

####################################################################################################################################

# Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different numbers 

# Lambda function to check if the number is Positive, Negative, or Zero 

check_number = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero' 

  

# Testing the lambda function with different numbers 

print(check_number(10))   # Output: Positive 

print(check_number(-5))   # Output: Negative 

print(check_number(0))    # Output: Zero 

 
"""
Chapter 2
Name: Ajeet
Collaborators: None
Time spent:

---------------------------------------
"""
"""
Excercise

# 0. After the following statements, what are the values of x and y?

x = 15
y = x
x = 22

Answer: When y = x at the second statement, the value of y became 15. At 3rd statement, the value of x chanaged to 22, but the value of y remained at 15.
So, x = 22, y =15
"""

# 2. Take the sentence: All is well.
# Store each word in a separate variable, then print out the sentence on one line using print.
a = "All"
b = "is"
c = "well"
print(a,b,c)

# Running  print(a, " ", b, " ", c)  will put extra space in the output

# 3. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

print(6 * (1 - 2))


# 4. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
# A = P(1+r/n)**nt
# where P = Principle amount ( initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is 
# Write a Python program that assigns the principal amount of $10000 to variable P,
# # assign to n the value 12, and assign to r the interest rate of 8%.
# # Then have the program prompt the user for the number of years t that the money will be compounded for.
# # Calculate and print the final amount after t years.





"""
--------------------------------------
Concepts from Book:

1. When we show the value of a string using the print function, the quotes are not present in the output.
Run print("Hello, World") as script. The output will just Hello, World without quotes.
Run print("Hello, World") in the Python interpreter or shell.  The output will be same just Hello, World without quotes.

But running "Hello, World" without print function in the Python interpreter will produce output with single quotes:  'Hello, World'

2. Strings in Python can be enclosed in either single quotes (') or double quotes (" - the double quote character),
or three of the same separate quote characters -  ''' or """

# Triple quoted strings can even span multiple lines.
"""

3. Data Types are also called Class

4. Order of Operations: https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/OrderofOperations.html
Multiplication and division both operators have the same precedence. Addition and Substraction both operators have the same precedence.
Operators with the same precedence (except for **) are evaluated from left-to-right. In algebra we say they are left-associative.
So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5.

An exception to the left-to-right left-associative rule is the exponentiation operator **.
A useful hint is to always use parentheses to force exactly the order you want when exponentiation is involved.

print(2 ** 3 ** 2)   # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!

5. assignment token:  = is Python’s assignment token, which should not be confused with the mathematical comparison operator using the same symbol.

----------------------------------------------
"""
"""
Chapter 1
Name: Ajeet
Collaborators: None
Time spent:

---------------------------------------
"""

"""

1. Write an English sentence with understandable semantics but incorrect syntax.
Write another English sentence which has correct syntax but has semantic errors.

Solution:
 - Understandable semantics but incorrect syntax
    i am a good boy
- Correct syntax but has semantic errors
    I am a boy good.

2. (a)Type 6 + 4 * 9 at the Python prompt/terminal/commandPrompt and hit enter. Record what happens.

    (b) Now create a Python script with the following contents:
    6 + 4 * 9
    What happens when you run this script?

    (c) Now change the script contents to:  print(6 + 4 * 9)
    and run it again. What happened this time?


Solution:
(a) I get the answer 42 automatically once I hit Enter. It is just like calculator, if you type this expression you’ll get the result 42

(b) I created a python script, named it as "solution.py" and put 6 + 4 * 9, and ran it.
The script ran successfully without any error but I did not get the result 42.

(c)  I created a python script, named it as "solution_print.py" and put print(6 + 4 * 9), and ran it.
The script ran successfully and got the result 42.
This means it is necessary to use the `print` function to make the answer show up
"""
print(6 + 4 * 9)


"""
--------------------------------------
Concepts from Book:

If there is a single syntax error anywhere in your program, Python will display an error message and quit,
and you will not be able to run your program.  Python can detect the syntax error by looking at the code without running it.
For example, in English, a sentence must begin with a capital
letter and end with a period. this sentence contains a syntax error. So does this one

If there is a semantic error in your program, it will run successfully, in the sense that the computer will not
generate any error messages, but it will produce the output you wanted to see.
Specifically, it will do what you told it to do by writing the program.
Its semantics(the meaning of the program) is wrong.
For example, a programmer wants to convert 25 to percentage, but he forgets to divide 25 by 100 when printing a percentage amount.
So, his intention was to see the 25% as output, but the code he wrote missed the division by 100,
and that is why Python did not produced the output as percentage, rather it produced wht the programmer wrote in the script

Runtime Error: the error does not appear until you run the program. These errors are also called exceptions
because they usually indicate that something exceptional (and bad) has happened.
 Type `cheese` without the quotation marks. The output will look something like this:
"NameError: name 'cheese' is not defined".
Specifically, it is a NameError, and even more specifically, it is an error because the name cheese is not defined.


semantic error
    An error in a program that makes it do something other than what the programmer intended.
semantics
    The meaning of a program.
syntax
    The structure of a program.
syntax error
    An error in a program that makes it impossible to parse — and therefore impossible to interpret.

"""
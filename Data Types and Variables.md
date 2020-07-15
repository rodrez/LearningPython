Data Types and Variables
========================

Intro
-----

Now that we are professional programmers and can hack Facebook and printers for our cousins and aunties (just kidding). It's a great time to learn more about how computers can categorize, store and use this data. We will also learn how to get input from the user and use that input to interact with our programs.

Strings
-------

When we write string in Python we can write within double quotes ("") or single quotes (''). It is very important to note that the quotes tells the computer where does the string begin and where does it ends. That being said if you use double quote to start and finish your string you cannot use double quotes inside the string. Now you may ask... But what if a sentence needs both double and single quotes? Great question!

We can use escape sequence but more on that later 😛

Escape Sequences
----------------

Escape sequences allows us to be more flexible whenever we want to use special character in a string. Normally an escape sequence is a combination of 2 characters a backslash and another character, for example: `\n` which inserts an additional line or "enter".

There are various escape sequences we can use with Python below are a few:

- `\\` - displays only one backslash. Why? Because the backslash is a special character in Python. In order to print a backslash we need to "escape" the backslash with another one.

- `\'` - displays single quote even if you started the string with single quotes
- `\"` - just like the one above but with double quotes 😄
- `\n` - Our old friend the new line! Pretty simple adds a new line.
- `\t` - adds a horizontal tab. Moves the cursor forwards one tab.

Number Types
------------

Python allows us to use different types of numbers, and two of the most common are called "floats" and "integers"

- floats - are any numbers that have a decimal point and their key word is `float`
- integers - are any numbers that DO NOT have decimal points.
# The are multiple ways to print multiple values when using the print function

# The first approach would be using commas
print('Luke', 'I am', 'your father')
print('Luke I am your father')

# The second approach we will cover is using + sign (this is called concatenation)
print('Superhero landing!' + ' She\'s going to do' + ' a superhero landing!')
print('Superhero landing! She\'s going to do a superhero landing!')

# Taking in consideration the examples above we can see that the result is the same although the approach is different.

# In exmaple 1 we uses commas to print multiple values. Notice how although we did not add spaces in front of 'I am' and 'your father', 
# python still added the empty spaces in the output.
# In example 2 , we use the '+' sign to concatenate the multiple values. Since we are concatenating the values it will print out the string as we pass type it.
# If we were to not add the empty spaces in front of each word, the output would be all together without spaces.

# BONUS CONTENT!
# We can also print the same statement multiple times uses the "*"
print("I am a program, and no, I can't hack you ex's Facebook account. At least not yet. LOL\n" * 2)

# The line of code above is quite peculiar. We have our normal print function and our string inside. 
# However, at the end we have '* 2', and you might be thinking since when we can multiple sentences. 
# But you forgot something, we are programmers and we can do this kind of stuff. 
# By using '* 2' we are telling Python... "Hey Python!, you know I am lazy and I would love to print this sentence twice but I don't want to type it twice."
# And since Python is so awesome we can just use "* 2" and that is it! Simple enough right 

######
# Now is your turn to create a program that prints a sentence as many time as you'd like.
# To make it more interesting you can also add some concatenation in there. Come on you got this!
######
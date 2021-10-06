#!/usr/bin/env python
# coding: utf-8

# In[16]:

# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = input('What is your favorite day of the week?')

if day_of_week.lower() == 'monday':
    print('Your favorite day of the week is Monday???')
else:
    print(f'Your favorite day of the week is {day_of_week}.')


# In[20]:


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = input('Please enter a day of the week. ')

if day_of_the_week.lower() in ['saturday','sunday']:
    print(f'{day_of_the_week} is a weekend.')
elif day_of_the_week.lower() in ['monday', 'tuesday','wednesday','thursday','friday']:
    print(f'{day_of_the_week} is a weekday.')
else:
    print('invalid input')


# In[38]:


# c. create variables and make up values for
#    the number of hours worked in one week
#    the hourly rate
#    how much the week's paycheck will be
#    write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

weekly_hours = 54
hourly_rate = 45
week_paycheck = 0
if weekly_hours <= 40:
    week_paycheck = weekly_hours * hourly_rate
else:
    week_paycheck = (40 * hourly_rate) + ((weekly_hours - 40) * (hourly_rate * 1.5))
print(week_paycheck)
    


# In[39]:


# 2. Loop Basics

# a. While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1


# In[45]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

num = 0
while num <= 100:
    print(num)
    num += 2
    


# In[46]:


# Alter your loop to count backwards by 5's from 100 to -10.

num = 100
while num >= -10:
    print(num)
    num -= 5


# In[47]:


# Create a while loop that starts at 2, and displays the number squared on each line while the number is 
# less than 1,000,000.
num = 2
while num < 1000000:
    print(num)
    num = num**2
    


# In[48]:


# Write a loop that uses print to create the output shown below.
num = 100
while num > 0:
    print(num)
    num -= 5


# In[62]:


# b. For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:

num = input('Please enter a number. ')
for i in range(1,11):
    print(f'{num} x {i} = {i * int(num)}')


# In[63]:


# ii. Create a for loop that uses print to create the output shown below.
for num in range(1,10):
    print(str(num) * num)


# In[29]:


# break and continue

# c. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting 
# the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the 
# continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

odd_number = input('Please enter an odd number between 1 and 50. ')

while True:
    if (odd_number.isdigit() == False
        or int(odd_number) > 50
        or int(odd_number) < 1
        or int(odd_number) % 2 == 0):
        print('Invalid input')
        odd_number = input('Please enter an odd number between 1 and 50. ')
    else:
        break

odd_number = int(odd_number)
for num in range(1, 51):
    if num % 2 == 0:
        continue
    elif num == odd_number:
        print(f'Yikes! Skipping number: {odd_number}.')
    else:
        print(f'Here is an odd number: {num}.')
                                                                      


# In[44]:


# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to
# enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value 
# the user entered is a valid number, also note that the input function returns a string, so you'll need to convert
# this to a numeric type.)


while True:
    positive_num = input('Please enter a positive number. ')
    if (positive_num.isdigit() == False
        or int(positive_num) <= 0):
        print('Invalid input')
    else:
        break

for num in range(0, int(positive_num) + 1):
    print(num)


# In[79]:


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the 
# number the user entered down to 1.

positive_int = int(input('Please enter a positive number. '))
counter = positive_int
while counter >= 1:
    print(counter)
    counter -= 1


# In[80]:


# 3. One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran 
# Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(0,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


# In[13]:


# 4. Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


cont = 'y'
while cont == 'y':
    integer = int(input('Please enter a number. '))
    print(f'Here is your table! \n \n number | squared | cubed \n -------|---------|--------')
    for num in range(1, integer + 1):
        print(f' {num}      |{num**2}        |{num**3}       ')
    cont = input('Do you want to continue? y/n ')


# In[45]:


# 5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

cont = 'y'
while cont == 'y':
    grade = int(input('Please enter your grade (0 - 100). '))
    if grade <= 100 and grade >= 88:
        print('A')
    elif grade < 88 and grade >= 80:
        print('B')
    elif grade < 80 and grade >= 67:
        print('C')
    elif grade < 67 and grade >= 60:
        print('D')
    else:
        print('F')
    cont = input('Would you like to continue? y/n ')


# In[58]:


# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the 
# list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in 
# that genre.

my_list_of_books = [{'title' : 'Atomic Habits', 'author': 'James Clear', 'genre' : 'productivity'}, 
                    {'title' : 'The Alchemist', 'author': 'Paulo Coelho', 'genre' : 'fiction'},
                    {'title' : 'Atlas Shrugged', 'author': 'Ayn Rand', 'genre' : 'fiction'},
                    {'title' : 'Einstein', 'author': 'Walter Isaacson', 'genre' : 'biography'}]

for book in my_list_of_books:
    print(book)
    

book_genre = input('Please enter a genre. ')
books_in_genre = []
for book in my_list_of_books:
    if book_genre == book['genre']:
        books_in_genre.append(book['title'])
if len(books_in_genre) > 0:
    print(books_in_genre)
else:
    print('Sorry, that genre does not exist in this library.')


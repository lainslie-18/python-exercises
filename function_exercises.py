#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string 2, `False` otherwise.

# In[3]:


def is_two(x):
    return x in [2, '2', 'two']
# print(is_two(24))


# 2. Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.

# In[40]:


def is_vowel(some_letter):
    return some_letter.lower() in 'aeiou'
# print(is_vowel('A'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[38]:


def is_consonant(some_letter):
    return not is_vowel(some_letter)
# print(is_consonant('a'))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[59]:


def capitalize_consonants(some_word):
    new_word = some_word.strip()
    if is_consonant(some_word[0]):
        return new_word.capitalize()
# print(capitalize_consonants(' puppies are the best!'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[24]:


def calculate_tip(tip_percentage, bill_total):
    return round(bill_total * tip_percentage, 2)
# print(calculate_tip(.3, 26.50))


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[26]:


def apply_discount(original_price, discount_percentage):
    return round(original_price * (1 - discount_percentage), 2)
# print(apply_discount(55, .25))


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[31]:


def handle_commas(num_str_w_commas):
    new_num_str = ''
    for num in num_str_w_commas:
        if num != ',':
            new_num_str += num
    return int(new_num_str)
# print(handle_commas('1,000,000'))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[35]:


def get_letter_grade(some_num):
    if some_num >= 88:
        return 'A'
    elif some_num >= 80:
        return 'B'
    elif some_num >= 67:
        return 'C'
    elif some_num >= 60:
        return 'D'
    else:
        return 'F'
        
# print(get_letter_grade(97))


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[41]:


def remove_vowels(some_str):
    new_str = ''
    for ch in some_str:
        if is_consonant(ch):
            new_str += ch
    return new_str
# print(remove_vowels('All around me are familiar faces,'))


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[53]:


def normalize_name(some_str):
    new_str = some_str.strip().lower()
    python_identifier = ''
    while new_str[0].isdigit():
        new_str = new_str[1:]
        
    for ch in new_str:
        if ch.isalnum():
            python_identifier += ch
        elif ch == ' ' or ch == '_':
            python_identifier += '_'
        else:
            continue
    
    if python_identifier[0] == '_':
        python_identifier = python_identifier[1:]
    return python_identifier

# print(normalize_name(' 2857 %ThIS is_My % teST STrInG '))


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[57]:


def cumulative_sum(num_list):
    sum_list = [num_list[0]]
    for num in num_list[1:]:
        sum_list.append(num + sum_list[-1])
    return sum_list
# print(cumulative_sum([10,9,7,4,0]))


# Bonus 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[73]:


def twelveto24(time_str):
    hh = time_str.split(':')[0]
    mm = ''
    am_pm = ''
    for ch in time_str.split(':')[1]:
        if ch.isdigit():
            mm += ch
        elif ch.isalpha():
            am_pm += ch
        else:
            continue
    if am_pm.lower() == 'am':
        return hh + ':' + mm
    else:
        return str(int(hh) + 12) + ':' + mm
    
# print(twelveto24('4:45pm'))


# In[83]:


def twentyfourto12(time_str):
    hh = int(time_str.split(':')[0])
    mm = int(time_str.split(':')[1])
    
    if hh == 0:
        return ('12') + ':' + str(mm) + 'am'
    elif hh == 12:
        return str(hh) + ':' + str(mm) + 'pm'
    elif 24 >= hh > 12:
        return str(hh - 12) + ':' + str(mm) + 'pm'
    elif 12 > hh > 0:
        return str(hh) + ':' + str(mm) + 'am'
    else:
        return 'invalid input'
    
# print(twentyfourto12('18:30'))


# Bonus 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27

# In[13]:


import string

def col_index(column_name): #XFD is the last returnable column
    alpha = list(string.ascii_uppercase)
    alpha2 = alpha.copy()
    
    for ch1 in alpha:
        for ch2 in alpha:
            alpha2.append(ch1 + ch2)
            
    for ch1 in alpha:
        for ch2 in alpha:
            for ch3 in alpha:
                alpha2.append(ch1 + ch2 + ch3) 

    column_dict = dict(list(zip(alpha2, range(1,16_385))))
    
    return column_dict[column_name.upper()]

# print(col_index('all'))


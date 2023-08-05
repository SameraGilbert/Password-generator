

import random
import string 

# Function to call on characters to build password 
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits 
    special = string.punctuation
 
# Password will always contain letters. The special characters/digits can be optional. Creating character variable assigned to letters with options o inlcude special characters / digits
# If statements combine digtis and characters to chracter variable which allows us to select from these when generating password
    characters = letters 
    if numbers:
        characters += digits 
    if special_characters:
        characters += special 

 # Create loop to generate characters to meet the password criteria

 # Password variable to store the password in 
    pwd = ""
# Criteria variable set to be able to later check if the criteria is met 
    meet_criteria = False 
 # Variables that chaeck for special chracters and digits 
    has_number = False 
    has_special = False 

# When you don't meet the criteria or equal password length contnue adding characters to password 
 # new char  is variable creating new password
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
    # checking   if the digits or special characters is included     
        if new_char in digits:
            has_number = True 
        elif new_char in special:
            has_special = True
# Checking if the criteria is true 
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
# adding meet criteria here to ensure that the check for special character doesnt continue as number criteria not met 
        if special_characters:
            meet_criteria = meet_criteria and has_special


    return pwd

# User input interface 
min_length = int(input("Enter  the minimum length:  "))
#Check if you want the lower and special numbers
has_number = input("Do you want to have numbers(y/n)? ").lower() == "y"
has_special= input("Do you want to have special characters (y/n)? ").lower() == "y"


pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)


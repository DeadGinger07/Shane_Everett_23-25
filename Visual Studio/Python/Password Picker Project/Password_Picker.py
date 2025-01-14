import random
import string

#The following is adjectives used by the application
adjectives = ['Silly', 'Adventurous', 'Confident', 'Stanky', 'Frantic', 'Ambitious', 'Cheerful', 'Sincere', 'Calm', 'Sincere', 'Adaptable', 'Helpful', 'Clever', 'Loving', 'Optimistic']

#The following are nouns used by the application
nouns = ['Francis', 'School', 'Prison', 'House', 'Bank', 'FortniteBattlePass', 'Yeast', 'Hotel', 'Jake', 'Jeff', 'Bill', 'Mickey', 'Donald', 'Michael', 'Nelson']

#The following are numbers used by the application
numbers = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75']

#The following are special_characters used by the application
special_characters = ['@', '$', '#', '!', '%', '^', '&', '*', '(', ')', ';', ':', '|', '~', '?']

#this is key
number_of_passwords = None

#This is the first thing the end user should see
print("Welcome to the password picker, where we help you choose a password!\n")
number_of_passwords = int(input("How many passwords would you like to generate today?\n"))

#for a loop
while True:

    for num in range(number_of_passwords):

#This is used to tell the application to choose a random selection from each category
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.choice(numbers)
        special_character = random.choice(special_characters)

    #This is the equation for a password
        password = adjective + noun + number + special_character
    
        print("Your new password is: %s " % password)

    response = input("\nWould you like a different password? Type y or n: ").lower()

    if response == 'n':
            break

    number_of_passwords = int(input("How many passwords would you like to generate today?\n"))


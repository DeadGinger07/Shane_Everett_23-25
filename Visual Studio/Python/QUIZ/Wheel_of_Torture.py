import random
#Welcome to the code to Wheel of Torture, a game where you have 9 chances to guess the word correctly before you die. Basically torture but ripping off Wheel of Fortune, hooray!
print('Wheel of Torture')
#This is the life count, it is required for the life count to work, and must be set to 9 when game is first ra.
lives = 9
def stringlength(string):
    counter = 0
    for x in string:
        counter+=1
    return counter
def secretworddef(clue):
    for x in range(0,stringlength(secret_word)):
            clue.append("?")
#this is the word list, DO NOT LET THEM APPEAR UNLESS GUESSED CORRECTLY!
words = ('Potato', 'New York', 'Windows', 'Mac OS', 'Tomato', 'Donald', 'Shrek', 'Rick', 'Morty', 'Donkey', 'Mario', 'Meme')
#the secret word should be randomly generated
secret_word = random.choice(words)
clue = list('')
secretworddef(clue)
#this contains data for the life count.
heart_symbol = u'\26C4'
guessed_score_correctly = False


#This is the functions that are needed to make Wheel of Torture work.
def update_clue (guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
while lives > 0:
    print(clue)
    
    #this prints the live count
    print('lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the word itself: ')
    #This tells you if it was right or wrong
    if guess == secret_word:
        guessed_score_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('The following you just entered was incorrect. 1 less life for you.')
        lives = lives - 1
    if '?' in clue:
        print('Yes')  
    else:
        guessed_word_correctly = True
        break
#here is if end user wins the game.
if guessed_score_correctly:
    print('Congratulations! The secret word was in fact ' + secret_word)
    #now for loose message
else:
    print('Congratulations! You blew up! The secret word was ' + secret_word)
#Algorithm can be found at https://docs.google.com/document/d/1gOuVXf_nJyzSSMnvDzqcjmuQL-8xm7Qh6jkQEwIvR1Y/edit?usp=share_link

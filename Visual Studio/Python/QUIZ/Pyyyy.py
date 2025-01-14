import random
trash_talk = ["Come on! Bill Gates did better than you!", "Are you serious? You should know this one", "Wow. Are you really not able to figure this out?"]
correct_response = ["Correct!", "You got this one right!", "Wow, you must really know a lot about Microsoft!", "Wow, Bill Gates is impressed!"]
#Here is the start of the code
print("WARNING: This game is case sensitive. Please make sure the first letter of any word is capitalized, because it's just common sense and also proper grammar too.")
#This game is meant to be a bit rude toward the player, however, this program does not intend to be offensive in any form.
print("Welcome to Who wants to be broke. The game where you answer questions but do not win any money, nor loose any, because money no longer exists when you are at Microsoft.")

#This is the start of the scoring code
#Microsoft facts are found on google, however, end user is asked to not use google for the answers.

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess == answer:
            print("{}".format(str(random.choice(correct_response))))
            
#This is the score equation
            score = score + 1
            still_guessing = False

#This shows how many chances the end user will get to answer them all correctly
        else:
            if attempt < 2:
                guess = input("{}".format(str(random.choice(trash_talk))))
            attempt = attempt + 1
    if attempt == 3:
        print('Come on! Phil Spencer got this one correct on his first try! The answer was : ' + answer)
        print("You have officially disappointed everyone at Microsoft.")

#This is the default score total
score = 0

#These are the questions
guess1 = input('When was Microsoft founded?')
check_guess(guess1, 'April 4th, 1975')
print('Your score is: %s' % score)

guess2 = input('When was Windows 1.0 first released?')
check_guess(guess2, 'November 20th, 1985')
print('Your score is: %s' % score)

guess3 = input('Which 2 people founded Microsoft?')
check_guess(guess3, 'Bill Gates and Paul Allen')
print('Your score is: %s' % score)

guess4 = input('When did Microsoft first release the original Xbox?')
check_guess(guess4, 'November 15th, 2001')
print('Your score is: %s' % score)

guess5 = input('What was the Xbox 360 best known for?')
check_guess(guess5, 'Red Ring of Death')
print('Your score is: %s' % score)

guess6 = input('Which version of Windows is considered by people to be the best version of all time?')
check_guess(guess6, 'Windows 7')
print('Your score is: %s' % score)

guess7 = input('What company did Microsoft buy from Nintendo for $375 million?')
check_guess(guess7, 'Rare')
print('Your score is: %s' % score)

guess8 = input('What accessory did Microsoft make to compete with Nintendo`s motion controls?')
check_guess(guess8, 'Kinect')
print('Your score is: %s' % score)

guess9 = input('Who is the current CEO of Microsoft?')
check_guess(guess9, 'Satya Nadella')
print('Your score is: %s' % score)

guess10 = input('Who is the current CEO of the Xbox Game Studios division?')
check_guess(guess10, 'Phil Spencer')
print('Your score is: %s' % score)

guess11 = input('Which company did Microsoft pay the most to aquire?')
check_guess(guess11, 'Activision Blizzard')
print('Your score is: %s' % score)

guess12 = input('What Microsoft game is best known on Xbox?')
check_guess(guess12, 'Halo')
print('Your score is: %s' % score)

guess13 = input('What is the most recent version of Windows?')
check_guess(guess13, 'Windows 11')
print('Your score is: %s' % score)

guess14 = input('What handheld did Microsoft last make games for?')
check_guess(guess14, 'DS')
print('Your score is: %s' % score)

guess15 = input('How old is Microsoft?')
check_guess(guess15, '48')
print('Your score is: %s' % score)

#This is for the score total
print('Congratulations! You got %s out of 15 Correct. Now get out of here!' % score)

#This is the end of the code

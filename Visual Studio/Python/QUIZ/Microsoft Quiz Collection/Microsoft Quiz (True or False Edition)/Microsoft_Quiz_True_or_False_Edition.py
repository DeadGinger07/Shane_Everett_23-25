import random

trash_talk = ["Come on! Bill Gates did better than you!", "Are you serious? You should know this one", "Wow. Are you really not able to figure this out?"]
correct_response = ["Correct!", "You got this one right!", "Wow, you must really know a lot about Microsoft!", "Wow, Bill Gates is impressed!"]
#Here is the start of the code
print("WARNING: This game is case sensitive. Please make sure the first letter\n \
of any word is capitalized, because it's just common sense and also proper grammar\n \
too.")
#This game is meant to be a bit rude toward the player, however, this program does not intend to be offensive in any form.
print("Welcome to the Microsoft quiz. The game where you answer true and false\n \
questions but do not win any money, nor loose any, because money no longer\n \
exists when you are at Microsoft.")
#The following message is exclusive to the True or False Edition:
print("Notice: This is the True or False Edition. The questions\n \
have been altered to fit in a true or false scenario.")

#This is the start of the scoring code
#Microsoft facts are found on google, however, end user is asked to not use google for the answers.

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 1:
        if guess == answer:
            print("{}".format(str(random.choice(correct_response))))
            
#This is the score equation
            score = score + 1
            still_guessing = False

#This shows how many chances the end user will get to answer them all correctly
        else:
            if attempt < 1:
                guess = print("{}".format(str(random.choice(trash_talk))))
            attempt = attempt + 1
    if attempt == 1:
        print('Come on! Phil Spencer got this one correct on his first try! The answer was : ' + answer)
        print("You have officially disappointed everyone at Microsoft.")

#This is the default score total
score = 0

#All of these answers came from a quick google search, while there was some obtained from the following link:
#https://en.wikipedia.org/wiki/Microsoft?scrlybrkr=5e880216#History

#These are the questions
guess1 = input('Microsoft was founded April 4th, 1975\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess1, 'T')
print('Your score is: %s' % score)

guess2 = input('Windows 1.0 first released back in November of 1975\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess2, 'F')
print('Your score is: %s' % score)

guess3 = input('Bill Gates and Phil Spencer founded Microsoft together back in 1975 \n \
Type T or F and press enter on your keyboard: ')
check_guess(guess3, 'F')
print('Your score is: %s' % score)

guess4 = input('The Xbox released November 15th, 2001\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess4, 'T')
print('Your score is: %s' % score)

guess5 = input('The Xbox 360 was best known for the Red Ring of Death\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess5, 'T')
print('Your score is: %s' % score)

guess6 = input('Windows 7 is considered to be the best version of windows to date by many\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess6, 'T')
print('Your score is: %s' % score)

guess7 = input('Microsoft bought Nintendo and all their studios\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess7, 'F')
print('Your score is: %s' % score)

guess8 = input('Microsoft was the creator of the Kinect\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess8, 'T')
print('Your score is: %s' % score)

guess9 = input('The Current ceo of microsoft is Satya Nadella\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess9, 'T')
print('Your score is: %s' % score)

guess10 = input('The current president of Xbox game studios is Doug Bowser\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess10, 'F')
print('Your score is: %s' % score)

guess11 = input('The most expensive aquisition Microsoft has ever made was Bethesda\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess11, 'F')
print('Your score is: %s' % score)

guess12 = input('Microsoft is best known for the Halo series\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess12, 'T')
print('Your score is: %s' % score)

guess13 = input('The most recent version of Windows is Windows 11\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess13, 'T')
print('Your score is: %s' % score)

guess14 = input('Microsoft last made handheld games for the PSVita\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess14, 'F')
print('Your score is: %s' % score)

guess15 = input('Microsoft is 48 years old\n \
Type T or F and press enter on your keyboard: ')
check_guess(guess15, 'T')
print('Your score is: %s' % score)

#This is for the score total
print('Congratulations! You got %s out of 15 Correct. Now get out of here!' % score)
input("Press Enter to close the game...")

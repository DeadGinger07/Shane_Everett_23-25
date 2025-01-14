import random

trash_talk = ["Come on! Bill Gates did better than you!", "Are you serious? You should know this one", "Wow. Are you really not able to figure this out?"]
correct_response = ["Correct!", "You got this one right!", "Wow, you must really know a lot about Microsoft!", "Wow, Bill Gates is impressed!"]
#Here is the start of the code
print("WARNING: This game is case sensitive. Please make sure the first letter of any word is capitalized, because it's just common sense and also proper grammar too.")
#This game is meant to be a bit rude toward the player, however, this program does not intend to be offensive in any form.
print("Welcome to the Microsoft quiz. The game where you answer questions but do not win any money, nor loose any, because money no longer exists when you are at Microsoft.")


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

#All of these answers came from a quick google search, while there was some obtained from the following link:
#https://en.wikipedia.org/wiki/Microsoft?scrlybrkr=5e880216#History

#These are the questions
guess1 = input('When was Microsoft founded?\n \
A)November 20th, 1985 B)November 15th, 2001 C)April 4th, 1975 D)I do not know\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess1, 'C')
print('Your score is: %s' % score)

guess2 = input('When was Windows 1.0 first released?\n \
A)November 20th, 1986 B)November 20th, 1984 C)November 20th, 2000 D)November 20th, 1985\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess2, 'D')
print('Your score is: %s' % score)

guess3 = input('Which 2 people founded Microsoft?\n \
A) Bill Gates & Paul Allen B) Steve Ballmer & Phil Spencer C)Satya Nadella & John W. Thompson D)None of the above\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess3, 'A')
print('Your score is: %s' % score)

guess4 = input('When did Microsoft first release the original Xbox?\n \
A) November 10th, 2020 B)November 15th, 2001  C)November 22nd, 2013 D) November 22nd, 2005\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess4, 'B')
print('Your score is: %s' % score)

guess5 = input('What was the Xbox 360 best known for?\n \
A)HD graphics B)HD DVD support C) Red Ring of Death D) Being the first 7th gen console released\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess5, 'C')
print('Your score is: %s' % score)

guess6 = input('Which version of Windows is considered by people to be the best version of all time?\n \
A)Windows XP B)Windows 10 C) Windows 7 D) Windows 95\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess6, 'C')
print('Your score is: %s' % score)

guess7 = input('What company did Microsoft buy from Nintendo for $375 million?\n \
A)Nintendo B)The Pokémon Company C)Monolith Soft D)Rare\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess7, 'D')
print('Your score is: %s' % score)

guess8 = input('What accessory did Microsoft make to compete with Nintendo`s motion controls?\n \
A)Wii Remote B)Playstation Move C)VR D)Kinect\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess8, 'D')
print('Your score is: %s' % score)

guess9 = input('Who is the current CEO of Microsoft?\n \
A)Bill Gates B)Steve Ballmer C)Paul Allen D) Satya Nadella\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess9, 'D')
print('Your score is: %s' % score)

guess10 = input('Who is the current CEO of the Xbox Game Studios division?\n \
A)Bill Gates B)Phil Spencer C)Joe Biden D)Doug Bowser\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess10, 'B')
print('Your score is: %s' % score)

guess11 = input('Which company did Microsoft pay the most to aquire?\n \
A)Bethesda B)Mojang C)Activision Blizzard D)Rare\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess11, 'C')
print('Your score is: %s' % score)

guess12 = input('What Microsoft game is best known on Xbox?\n \
A)Halo B)Gears of War C)Forza D)Fable\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess12, 'A')
print('Your score is: %s' % score)

guess13 = input('What is the most recent version of Windows?\n \
A) Windows 10 B)Windows 11 C) Windows 9 D) Windows 12\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess13, 'B')
print('Your score is: %s' % score)

guess14 = input('What handheld did Microsoft last make games for?\n \
A)Sony PSP B)GameBoy Advance C)Nintendo Switch D)Nintendo DS\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess14, 'D')
print('Your score is: %s' % score)

guess15 = input('How old is Microsoft?\n \
A)58 B)48 C)100 D)37\n \
Type A, B, C, or D and press enter on your keyboard: ')
check_guess(guess15, 'B')
print('Your score is: %s' % score)

#This is for the score total
print('Congratulations! You got %s out of 15 Correct. Now get out of here!' % score)
input("Press Enter to close the game...")

# PASTE YOUR WOFPlayer CLASS (from part A) HERE
# PASTE YOUR WOFHumanPlayer CLASS (from part B) HERE
# PASTE YOUR WOFComputerPlayer CLASS (from part C) HERE


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

# Repeatedly asks the user for a number between low & high (inclusive)
def getNumberBetween(prompt, low, high):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < low:
                errmessage = 'Must be at least {}'.format(low)
            elif n > high:
                errmessage = 'Must be at most {}'.format(high)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = f'{userinp} is not a number.'

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input(f'{errmessage}\n{prompt}')

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

# GAME LOGIC CODE
print('='*15)
print('WHEEL OF PYTHON')
print('='*15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)
num_computer = getNumberBetween('How many computer players?', 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

# Create the player instances
human_players = [WOFHumanPlayer(input('Enter the name for player #{}'.format(i+1))) for i in range(num_human)]
computer_players = [WOFComputerPlayer('Computer {}'.format(i+1), difficulty) for i in range(num_computer)]
players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print('We need players to play!')
    raise Exception

category, phrase = getRandomCategoryAndPhrase()
guessed = []

playerIndex = 0

winner = False
while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2)
    print('{}!'.format(wheelPrize['text']))

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'cash':
        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper()
        if move == 'EXIT':
            break
        elif move != 'PASS':
            if len(move) == 1:
                if move not in LETTERS:
                    print('Guesses should be alphanumeric. Try again.')
                    continue
                if move in guessed:
                    print('{} has already been guessed. Try again.'.format(move))
                    continue

                if move in VOWELS:
                    if player.prizeMoney < VOWEL_COST:
                        print('Need {} to guess a vowel. Try again.'.format(VOWEL_COST))
                        continue
                    else:
                        player.prizeMoney -= VOWEL_COST

                guessed.append(move)

                print('{} says "{}"'.format(player.name, move))

                count = phrase.count(move)
                if count > 0:
                    if count == 1:
                        print("There is one {}".format(move))
                    else:
                        print("There are {} {}'s".format(count, move))

                    player.addMoney(count * wheelPrize['value'])

                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])

                    if obscurePhrase(phrase, guessed) == phrase:
                        winner = player
                        break

                    continue

                elif count == 0:
                    print("There is no {}".format(move))
            else:
                if move == phrase:
                    player.addMoney(wheelPrize['value'])
                    if wheelPrize['prize']:
                        player.addPrize(wheelPrize['prize'])
                    winner = player
                    break
                else:
                    print('{} was not the phrase'.format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won.')

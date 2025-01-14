def menu():
    print()
    print("Welcome to our madlibs compalation!")
    print()
    print("Breckin(1), Shane(2), Tacota(3), Saint(4)")
    print()
    answer = input("Select whose madlib you want to do: ")

    if answer == "1":
        print()
        breckin()
    if answer == "2":
        print()
        shane()
    if answer == "3":
        print()
        tacota()
    if answer == "4":
        print()
        saint()
        
    else:
        print("That isn't a selection.")
        menu()

def breckin():
    noun1 = input("Please enter a noun: ")
    adjective1 = input("Please enter an adjective: ")
    occupation1 = input("Please enter an occupation: ")
    noun2 = input("Please enter a noun: ")
    adjective2 = input("Please enter an adjective: ")
    adjective3 = input("Please enter an adjective: ")
    puralnoun1 = input("Please enter a plural noun: ")
    noun3 = input("Please enter a noun: ")
    body1 = input("Please enter a part of the body: ")
    adverb1 = input("Please enter an adverb: ")
    alive1 = input("Please enter something alive: ")
    noun4 = input("Please enter a noun: ")
    alive2 = input("Please enter something alive (pural): ")
    adjective4 = input("Please enter an adjective: ")
    adjective5 = input("Please enter an adjective: ")
    noun5 = input("Please enter a noun: ")
    verb1 = input("Please enter a verb ending in \"ing\": ")

    print()

    print('An interview with the Headless Horseman:')
    print('Interviewer: Welcome to \"Interview with a/an ' + noun1 + '\"')
    print('Today we\'ll be interviewing a/an ' + adjective1 + ' creature, the')
    print('Headless ' + occupation1 + '! Your fans are wondering, what\'s it like')
    print('having a/an ' + noun2 + ' for a head?')
    print('Headless Horseman: It\'s absolutely ' + adjective2 + '. First I had to dig')
    print('out all the ' + adjective3 + puralnoun1 + ' that were inside it. Then')
    print('I used a/an ' + noun3 + 'to carve a new ' + body1 + '. On dark')
    print('nights, I\'ll ' + adverb1 + ' ride around on my ' + alive1 + ',')
    print('take off my ' + noun4 + ', and throw it at ' + alive2)
    print('to scare them!')
    print('Interviewer: Sounds ' + adjective4 + '!')
    print('Headless Horseman: But the most ' + adjective5 + ' part of being the')
    print('Headless Horseman is that I never have to buy a/an ' + noun5 + ' to')
    print('wear when I go trick-or-' + verb1 + ' on Halloween!')

    def restart():
        print()
        answer = input("do you want to restart? y/n")
        print()
        
        if answer == "y":
            menu()
        if answer == "n":
            quit()
        if answer == "Y":
            menu()
        if answer == "N":
            quit()
        else:
            print("thats not a selection")
            restart()
            
    restart()
            

def shane():
    noun1=input("Please enter a noun: ")
    pluralnoun1 = input("Please enter a plural noun: ")
    typeofbuilding1 = input("Please enter a type of building: ")
    verb1 = input ("Please enter a verb: ")
    pluralnoun2 = input("Please enter a plural noun: ")
    sillyword = input("Please enter a silly word: ")
    partofbody = input("Please enter a part of the body: ")
    noun2 = input("Please enter a noun: ")
    animal = input("Please enter an animal: ")
    noun3 = input("Please enter a noun: ")
    verbing = input("Please enter a verb ending in ing: ")
    typeoffood = input("Please enter a type of food: ")
    verb2 = input("Please enter a verb: ")
    Adjective = input("Please enter an adjective: ")
    typeofliquid = input("Please enter a type of liquid: ")
    exclamation = input("Please insert an exclamation: ")
    alive = input("Please enter something that is alive: ")
    noun4=input("Please enter a noun: ")

    print()

    print("Is there a creature living under your",noun1," ? Answer these",pluralnoun1,"")
    print("to find out if you're sharing your",typeofbuilding1," with a monster!")
    print("When you",verb1," at night, do you hear strange",pluralnoun2," that sound like",sillyword,"?")
    print("Have you ever sseen a hairy",partofbody," reaching out from under your",noun2,"?")
    print("Is your pet",animal," afraid to come into your bedroom at",noun3," -time?")
    print("Do you suspect something might be",verbing," all the",typeoffood," in your refridgerator")
    print("while you",verb2," ! Do you find pulles of",Adjective," ",typeofliquid," around your bedroom?")
    print("If you answered",exclamation," to any of these questions, you have a/an",alive," under your",noun4," .")

    def restart():
        print()
        answer = input("do you want to restart? y/n")
        print()
        
        if answer == "y":
            menu()
        if answer == "n":
            quit()
        if answer == "Y":
            menu()
        if answer == "N":
            quit()
        else:
            print("thats not a selection")
            restart()
            
    restart()

def tacota():
    noun = input("noun ")
    PartOfTheBodyPlural = input("Part Of The Body (Plural) ")
    PartOfTheBody = input("Part Of The Body ")
    animal = input("animal ")
    Number = input("Number ")
    noun2 = input("noun ")
    Adjective = input("Adjective ")
    TypeOfLiquid = input("Type Of Liquid ")
    TypeOfFoodPlural= input("Type Of Food(plural) ")
    verb = input("verb ")
    noun3 = input("noun ")
    Number2 = input("Number ")

    TypeOfContainer = input("Type Of Container ")
    VerbEndingInIng = input("Verb Ending In Ing ")
    noun4 = input("noun ")

    print()

    madlibs = "Hello, fellow witches! Here's a recipe to whip up a wicked "
    madlibs2 = noun + " That'll put a smile on those pesky kids' " + PartOfTheBodyPlural + " when they come to your door on halloween. " " take one " + PartOfTheBody + " of an " + animal + " and mix it with "+ Number + " pinches of " + noun2 
    madlibs3 =  " Pour in " + Adjective + " " + TypeOfLiquid + " and blend until it smells like fried "  + TypeOfFoodPlural 
    madlibs4 = verb + " all the ingredients in an iron " + noun3 + " once cooked put " + Number2 + " drops of the potion in a/an " + TypeOfContainer + " and give it to any child who comes to your door " + VerbEndingInIng + " for a yummy " + noun4 + "."

    print(str(madlibs))    
    print(str(madlibs2))
    print(str(madlibs3))
    print(str(madlibs4))
    
    def restart():
        print()
        answer = input("do you want to restart? y/n")
        print()
        
        if answer == "y":
            menu()
        if answer == "n":
            quit()
        if answer == "Y":
            menu()
        if answer == "N":
            quit()
        else:
            print("thats not a selection")
            restart()
            
    restart()

def saint():
    adjective1 = input('Please enter an adjective')
    noun1 = input('Please enter a noun')
    celebrity = input('Please enter a celebrity')
    number1 = input('Please enter a number')
    occupation = input('please enter a occupation')
    personInRoom = input('Please the name of a person in the room')
    sameCelebrity = input('Please enter the same celebrity you\'ve chosen')
    exclamation = input('Please enter an exclmation')
    adjective2 = input('Please enter an adjective')
    pluralNoun1 = input('Please enter a plural noun')
    partOfTheBody = input('Please enter a part of the body')
    number2 = input('Please enter a number')
    pluralNoun2 = input('Please enter a plural noun')
    adjective3 = input('Please enter an adjective')
    animal = input('Please enter an animal')
    sillyWord = input('Please enter a silly word')
    noun2 = input('Please enter a noun')
    adjective4 = input('Please enter an adjective')

    print()
    
    print('If you ever travel to Scotland, you might be', adjective1 ,'enough to catch a glimspe of the Loch Ness', noun1 ,'also affectionately known as', celebrity ,'Sightings of the creature date all the way back to the year', number1 ,' when, legend has it, a/an', occupation ,'named', personInRoom ,'rising from the lake and shouted,', exclamation ,'Since then, Loch Ness has been a/an', adjective2 ,'destination for', pluralNoun1 ,'traveling from all over the world. The creature is said to have a/an', partOfTheBody ,'nearly', number2 ,'feet tall and a body longer than twenty', pluralNoun2 ,'While many think the legend is just a/an', adjective3 ,'hoax, believers say the creature is actually some type of', animal ,'that was trapped in the lake during the', sillyWord ,'age. Whatever the truth may be, if you\'re lucky enough to take a photo of the', noun2 ,'you\'ll become one of the most', adjective4 ,'people in the world!' )

    def restart():
        print()
        answer = input("do you want to restart? y/n")
        print()
        
        if answer == "y":
            menu()
        if answer == "n":
            quit()
        if answer == "Y":
            menu()
        if answer == "N":
            quit()
        else:
            print("thats not a selection")
            restart()
            
    restart()

menu()


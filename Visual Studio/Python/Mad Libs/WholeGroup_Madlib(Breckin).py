print("Welcome to our Thanksgiving madlibs compalation!")
def menu():
    print()
    print("[1] Political Speech: by Breckin")
    print("[2] Capitalism: by Shane")
    print("[3] Thanksgiving Disaster: by Enoch")
    print("[4] Science Fair: by Jeremiah")
    print("[5] How Thanksgiving Became a Holiday: by Saint")
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
        enoch()
    if answer == "4":
        print()
        jeremiah()
    if answer == "5":
        print()
        saint()
        
    else:
        print("That isn't a selection.")
        menu()

def breckin():
    print()
    print("Political Speech: by Breckin")
    print()
    adjective1 = input("Please enter an adjective: ")
    adjective2 = input("Please enter an adjective: ")
    puralnoun1 = input("Please enter a plural noun: ")
    puralnoun2 = input("Please enter a plural noun: ")
    adjective3 = input("Please enter an adjective: ")
    noun1 = input("Please enter a noun: ")
    noun2 = input("Please enter a noun: ")
    puralnoun3 = input("Please enter a plural noun: ")
    adjective4 = input("Please enter an adjective: ")
    person_in_room = input("Please enter the name of a person in this room (male)")
    adjective5 = input("Please enter an adjective: ")
    noun3 = input("Please enter a noun: ")
    adjective6 = input("Please enter an adjective: ")
    noun4 = input("Please enter a noun: ")
    puralnoun4 = input("Please enter a plural noun: ")
    puralnoun5 = input("Please enter a plural noun: ")
    adjective7 = input("Please enter an adjective: ")
    adjective8 = input("Please enter an adjective: ")
    adjective9 = input("Please enter an adjective: ")

    print()

    print('Ladies and gentlemen, on this ' + adjective1 + ' occasion, it is a privilege')
    print('to address such a/an ' + adjective2 + '-looking group of ' + puralnoun1 + '.')
    print('I can tell from your smiling ' + puralnoun2 + ' that you will support my')
    print(adjective3 + ' program in the coming election. I promise that, if')
    print('elected, there will be a/an ' + noun1 + ' in every ' + noun2 + ',')
    print('and two ' + puralnoun3 + ' in every garage. I want to warn you against my')
    print(adjective4 + ' opponent, Mr. ' + person_in_room + '. The man is')
    print('nothing but a/an ' + adjective5 + noun3 + '. He has')
    print('a/an ' + adjective6 + ' character and is working ' + noun4)
    print('in glove with the criminal element. If elected, I promise to eliminate vice. I will')
    print('keep ' + puralnoun4 + ' off the city\'s street. I will keep crooks from dipping')
    print('their ' + puralnoun5 + ' in the public till. I promise you ' + adjective7)
    print('government, ' + adjective8 + ' taxes, and ' + adjective9 + ' schools.')
    print()
    print()

    ''' def restart():
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
            
    restart()'''
    menu()
            

def shane():
    print()
    print("Capitalism: by Shane")
    print()
    pluralnoun1 = input("Please enter a plural noun: ")
    adjective1 = input("Please enter an adjective: ")
    animal = input("Please enter an animal: ")
    noun1 = input("Please enter a noun: ")
    adjective2 = input("Please enter an adjective: ")
    adjective3 = input("Please enter an adjective: ")
    pluralnoun2 = input("Please enter a plural noun: ")
    noun2 = input("Please enter a noun: ")
    adjective4 = input("Please enter an adjective: ")
    noun3 = input("Please enter a noun: ")
    noun4 = input("Please enter a noun: ")
    adjective5 = input("Please enter an adjective: ")
    noun5 = input("Please enter a noun: ")
    pluralnoun3 = input("Please enter a plural noun: ")
    adjective6 = input("Please enter an adjective: ")
    noun6 = input("Please enter a noun: ")

    print()

    print("This is how I made one million",pluralnoun1,"in the stock market. It's")
    print("simple. At the present time, any",adjective1,"investor with a little capital")
    print("should be able to double his",pluralnoun1," in a few months. All the experts agree that we are")
    print("near the end of our",animal,"market. Just recently, for instance, the American",noun1,"and")
    print("Foundary Company has shown a/an",adjective2,"trend. Conditions indicate a/an",adjective3,"market")
    print("for their principal product, automatic",pluralnoun2,"International Telephone and",noun2,"Company")
    print("also looks",adjective4,". At the end of the last fiscal",noun3," , they were earning 10 dollars a/an",noun4,".")
    print("Another",adjective5,"tip is Consolidated",noun5," . This outfit manufactures and sells electronic",pluralnoun3,"of")
    print("a very",adjective6,"quality. But whatever you do, act now. Remember, prosperity is just around the",noun6,".")
    print()
    print()

    menu()

def enoch():
    print()
    print("Thanksgiving Disaster: by Enoch")
    print()
   # animals= input(': ')
   # profession = input('labor reconsiderer: ')
    cloth = input('Piece of clothing: ')
    things = input('Thing(plural): ')
    name= input('Name: ')
    place = input('Place: ')
    verb = input('Verb: ')
    food = input('Food: ')
    adjective = input('adjective: ')
    color = input('color: ')
    thing = input('thing:')
    place1 = input('place: ')
    person= input('person: ')
    adjective1 = input('adjective: ')
    insect= input('insect: ')
    food1 = input('food: ')
    verb1 = input('verb: ')
    print('I clearned the table for thankgiving diner ' + adjective + ' the food was ' + color+ ' with splotches of '+thing+ ' It looked terrible i went to the' + place+ ' with my bestfriend and '+person+'  who was a'  + adjective1 + insect + ' we bought some ' +food1 + ' when we got home''we decided to cook the food '+verb1 + ' and the food looked wonderful almost like ' +verb+ '.')    
    print()
    print()
    
    menu()

def jeremiah():
    print()
    print("Science Fair: by Jeremiah")
    print()
    def addWord(wordType):
        word = input("Please enter a(n) %s." % wordType)
        return word

    city = addWord("city")
    adverb = addWord("adverb")
    adjective = addWord("adjective")
    person_in_room = addWord("person in room(female)")
    noun = addWord("noun")
    silly_word = addWord("silly word")
    person_in_room2 = addWord("person in room(male)")
    adejctive2 = addWord("adjective")
    past_tense_verb = addWord("past tense verb")
    person_in_room3 = addWord("person in room")
    verb_ending_in_ing = addWord("verb ending in ing")
    number = addWord("number")
    color = addWord("color")
    adjective3 = addWord("adjective")
    noun2 = addWord("noun")
    adjective4 = addWord("adjective")

    print()
    print("Thank you all for participating in the",city,"Middle School Science Fair.")
    print("Everyone worked very",adverb,"on their projects and it shows. We will")
    print("now announce the first-, second-, and",adjective,"-place winner.")
    print(person_in_room,"won first prize for her miniature erupting",noun,",")
    print("which was a model of the largest volcano in history, Mount",silly_word,".")
    print(person_in_room2,"got seconf place for his super",adjective,"miniature")
    print("solar system, in which all the planets",past_tense_verb,"in circles.")
    print(person_in_room3,"was given third-place ribbon for",verb_ending_in_ing,"an ant")
    print("farm using sand and",number,"tiny",color,"ants. That's it for the",adjective3)
    print("annual science fair. We'll see you next",noun2,"for another round of")
    print(adjective4,"science experiments")

    print()
    print()
    menu()
            

def saint():
    print()
    print("How Thanksgiving Became a Holiday: by Saint")
    print()
    adjective1 = input('Please enter an adjective')
    pluralNoun1 = input('Please enter a plural noun')
    adjective2 = input('Please enter an adjective')
    place = input('Please enter a place')
    verb1 = input('Please enter a verb')
    adjective3 = input('Please enter an adjective')
    pluralNoun2 = input('Please enter a plural noun')
    pluralNoun3 = input('Please enter a plural noun')
    adjective4 = input('Please enter an adjective')
    adjective5 = input('Please enter an adjective')
    personInRoom = input('Please the name of a person in the room')
    adjective6 = input('Please enter an adjective')
    pluralNoun4 = input('Please enter a plural noun')
    print()

    print('Even though the first Thanksgiving took place in 1621, Thanksgiving didn\'t become a national holiday until a/an', adjective1 ,'woman named Sarah Josepha Hale came along. in the 1800s, Ms. Hale was one of the first female', pluralNoun1 ,'at a/an', adjective2 ,'magazine. She was famous throughout (the)', place ,'for her atricles encourging women to', verb1 ,'exercise and get a/an', adjective3 ,'education. But one of Sarah\'s biggest ideas was to make Thanksgiving a national holiday, to be celebrated by ', pluralNoun2 ,'across America. At the time, Thanksgiving was only celebrated by a few', pluralNoun3 ,'Sarah wrote', adjective4 ,'letters to one president after another, trying to convince them of how', adjective5 ,'Thanksgiving was. No one listened-at least not until President', personInRoom ,'He/She declared Thanksgiving a/an', adjective6 ,'holiday in 1863, and', pluralNoun4 ,'everywhere have been celebrating it ever since.')
    print()
    menu()

menu()


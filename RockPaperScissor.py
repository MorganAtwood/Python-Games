import random

def select():
    
    picks = {
        1:"Rock",
        2:"Paper",
        3:"Scissor"
    }
    print('1) Rock')
    print('2) Paper')
    print('3) Scissor')

    question = int(input('Please select your weapon: '))
    
    if question > 3 or question  < 1:
        input("That's not a choice!")
        select()
    #Answer was accepted   
    else:

        o = random.choice(list(picks))
    #Display picks
        print("You picked " + picks.get(question))
        print("I picked " + picks.get(o))

        
#If computer picks Rock
    if o == 1 and question == 1:
        print("Looks like we both picked Rock..")
    elif o == 1 and question == 2:
        print("You covered me, you win..")
    elif o == 1 and question == 3:
        print("ROCK SMASHES SCISSOR, I WIN!!")
#If computer picks Paper
    elif o == 2 and question == 1:
        print("Paper covers Rock, I win :)")
    elif o == 2 and question == 2:
        print("Looks like we tied..")
    elif o == 2 and question == 3:
        print("Dang, you cut me. You win this one..")
#If computer picks Scissor
    elif o == 3 and question == 1:
        print(":( You win...")
    elif o == 3 and question == 2:
        print("I cut your paper in half, I win!")
    elif o == 3 and question == 3:
        print("I like the way you think ;)")    
   
    again = input('Want to play again? (y/n)')
    if again == 'y':
        select()
    else:
        exit()



print("Welcome to Morgan's Rock, Paper, Scissors")
input("Press Enter to continue...")


select()




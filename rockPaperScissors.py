import random

def game():
    # User Function
    user = (input("Enter your choice:: ")).capitalize()
    if user == 'Rock' or user == 'Paper' or user == 'Scissors':
        # Computer's Function
        def bot():
            numb = random.randint(1, 3)
            if numb == 1: 
                return 'Rock'
            elif numb == 2:
                return "Paper"
            else:
                return 'Scissors'

        botchoice = bot()


        # Choice Declaration
        print(f'Computer Chooses {botchoice} and You Chooses {user}')

        # Game Function
        def choice():
            if user == "Rock" and botchoice == "Paper":
                print("You lose")
            elif user == "Paper" and botchoice == "Rock":
                    print('You Win')
            elif user == "Scissors" and botchoice == "Rock":
                print('You lose')
            elif user == "Rock" and botchoice == "Scissors":
                print('You Win')
            elif user == "Paper" and botchoice == "Scissors":
                print('You lose')
            elif user == "Scissors" and botchoice == "Paper":
                print('You Win')
            else:
                print("It is a Tie")

        choice()
    else:
        print("You Didn't make a Choice between Rock, Paper and Scissors")


# Rules
needRules = (input("Do you want to know rules(Y/N):: ")).upper()
if needRules == 'Y':
    rules = '''
    1.Players:
        The game is played between two players. In a single-player version, one player competes against the computer.

    2.Choices:
        Each player must choose one of three options: Rock, Paper, or Scissors.

    3.Winning Combinations:
        Rock vs. Scissors: Rock crushes Scissors. The player who chooses Rock wins.
        Scissors vs. Paper: Scissors cut Paper. The player who chooses Scissors wins.
        Paper vs. Rock: Paper covers Rock. The player who chooses Paper wins.

    4.Ties:
        If both players choose the same item (e.g., Rock vs. Rock), the game is a tie, and no one wins.

    5.Objective:
        The goal is to select the option that defeats your opponent's choice according to the rules above.
    '''
    print(rules)
    game()

else:
    game()
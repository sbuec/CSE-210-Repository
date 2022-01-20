from linecache import checkcache
from .dice import Dice


#GameSetup class is used to set up a set of steps the game goes through
#   and calls associated functions for those steps in imported files
class GameSetup:
    def __init__(self):
        self.rolls = []
        self.score = 0
        self.total = 0
        self.play_game = True

        for i in range(5):
            die = Dice()
            self.rolls.append(die)

    #Call the functions to run the program
    def start_game(self):
        while self.play_game:
            self.continue_game()
            self.newScore()
            self.rollScore()

    #Ask if user wants to continue playing
    def continue_game(self):

        check_continue = True
        while check_continue:
            checkRoll = input('Roll dice? [y/n]')
            
            if checkRoll == 'n':
                self.play_game = False
                check_continue = False
            elif checkRoll == 'y':
                self.play_game = True
                check_continue = False
            else:
                print(checkRoll + ' is not a valid option. Try again:')
                check_continue = True

    #Update player's score
    def newScore(self):
        if not self.play_game:
            return

        for i in range(len(self.rolls)):
            rolls = self.rolls[i]
            rolls.roll()
            self.total += rolls.points

    #Show rolled values and total score
    def rollScore(self):
        if not self.play_game:
            return

        values = ''
        for i in range(len(self.rolls)):
            roll = self.rolls[i]
            values += f'{roll.value} '

        print('Your rolls: ', values)
        print('Your total score: ', self.total)
        self.continue_game == (self.score > 0)
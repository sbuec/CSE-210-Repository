#Program must include README file
#Must include class and method comments
#Must have at least 2 classes
#Must follow specific game rules


'''
Game rules:
    Played with 5 dice
    Player asked 'Roll dice? [y/n]'
    Input y/Y or n/N
    Roll # = points:
        1 = 100
        5 = 50
    Show dice rolls and scores on screen
    If no 1's or 5's are rolled, game over
'''


from game.setup import GameSetup

game_setup = GameSetup()
game_setup.start_game()
# Created by Emma Hodor on 1/3/2023
# ASCII art generated using patorjk.com
import random

ASCII = """
                                                                                                                                                                    
                                                                         ____                            ,--.                                                       
  ,----..                                                              ,'  , `.                        ,--.'|                      ____                             
 /   /   \                                                          ,-+-,.' _ |                    ,--,:  : |                    ,'  , `. ,---,                     
|   :     :         ,--,                                         ,-+-. ;   , ||                 ,`--.'`|  ' :        ,--,     ,-+-,.' _ ,---.'|             __  ,-. 
.   |  ;. /       ,'_ /|           .--.--.   .--.--.            ,--.'|'   |  ;|                 |   :  :  | |      ,'_ /|  ,-+-. ;   , ||   | :           ,' ,'/ /| 
.   ; /--`   .--. |  | :   ,---.  /  /    ' /  /    '          |   |  ,', |  ':    .--,         :   |   \ | : .--. |  | : ,--.'|'   |  |:   : :     ,---. '  | |' | 
;   | ;  __,'_ /| :  . |  /     \|  :  /`./|  :  /`./          |   | /  | |  ||  /_ ./|         |   : '  '; ,'_ /| :  . ||   |  ,', |  |:     |,-. /     \|  |   ,' 
|   : |.' .|  ' | |  . . /    /  |  :  ;_  |  :  ;_            '   | :  | :  |, ' , ' :         '   ' ;.    |  ' | |  . .|   | /  | |--'|   : '  |/    /  '  :  /   
.   | '_.' |  | ' |  | |.    ' / |\  \    `.\  \    `.         ;   . |  ; |--/___/ \: |         |   | | \   |  | ' |  | ||   : |  | ,   |   |  / .    ' / |  | '    
'   ; : \  :  | : ;  ; |'   ;   /| `----.   \`----.   \        |   : |  | ,   .  \  ' |         '   : |  ; .:  | : ;  ; ||   : |  |/    '   : |: '   ;   /;  : |    
'   | '/  .'  :  `--'   '   |  / |/  /`--'  /  /`--'  /        |   : '  |/     \  ;   :         |   | '`--' '  :  `--'   |   | |`-'     |   | '/ '   |  / |  , ;    
|   :    / :  ,      .-.|   :    '--'.     '--'.     /         ;   | |`-'       \  \  ;         '   : |     :  ,      .-.|   ;/         |   :    |   :    |---'     
 \   \ .'   `--`----'    \   \  /  `--'---'  `--'---'          |   ;/            :  \  \        ;   |.'      `--`----'   '---'          /    \  / \   \  /          
  `---`                   `----'                               '---'              \  ' ;        '---'                                   `-'----'   `----'           
                                                                                   `--`                                                                             
"""

print(ASCII + '\n')


def guess():
    def rerun():
        while True:
            replay = input("Would you like to play again? Type 'y' or 'n': ")
            if replay == 'y':
                guess()
            elif replay == 'n':
                quit()
            else:
                print('Please type in valid input.\n')

    while True:
        difficulty = input(
            "Welcome to Guess My Number! Here you'll be guessing a number between 1 and 100. Type your difficulty - "
            "'easy' "
            "or 'hard': ").lower()
        if difficulty == 'easy':
            lives = 10
            break
        elif difficulty == 'hard':
            lives = 5
            break
        else:
            print('Please type in valid input.\n')

    number = random.randint(1, 101)

    while lives > 0:
        print(f'Lives: {lives}')
        user_chose = (input('Guess a number between 1 and 100: '))
        if user_chose.isdigit():
            user_chose = int(user_chose)
            if user_chose == number:
                print('You guessed the right number! Nice job!')
                rerun()
            elif user_chose < number:
                print('Your number is too low, guess again.')
                lives -= 1
            else:
                print('Your number is too high, guess again.')
                lives -= 1

    print('Oops, you ran out of lives, game over :(')
    quit()


guess()

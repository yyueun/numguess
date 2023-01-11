from random import shuffle,choice

result = {
        'stay to win' : 0,
        'move to win' : 0
        }
        '

doors = [0,0,1]
shuffle(doors)

user_choice = choice(doors)

if user_choice == 0:
    result['move_to_win'] += 1
else:
    result['stay_to_win] += 1

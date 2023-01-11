from random import shuffle,choice

result = {
        'stay to win' : 0,
        'move to win' : 0
        }
        '

doors = [0,0,1]

iter_num = int(input("원하는 횟수를 입력하세요 (100-10000): "))
#
for _ in range(iter_num):
    shuffle(doors)
    user_choice = choice(doors)

    if user_choice == 0:
        result['move_to_win'] += 1
    else:
        result['stay_to_win'] += 1
print("{} times run: stay-{stay_to_win} switch-{move_to_win}".format{iter_num**result}

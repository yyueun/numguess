## Numguess 게임을 시작합니다.
---------------------------------
from random import randint
from time import sleep

username= input("이름을 작성해주세요: ")
print(f"안녕하세요,{username}님! 1-100까지의 정수를 하나 맞춰주세요")


answer = random.randint(1,100)


user_answer = int(input("숫자를 입력해주세요 : ")
print(f'{username}님, 당신이 선택한 숫자는 {user_answer}입니다!')


print(f"정답은 {answer}이었습니다!")

#Compare answer with user's guess
if user_answer == answer:    
    print(*************)
    sleep(1)
    print(*************)
    sleep(1)
    print(*************)
    sleep(1)
    print(f'축하합니다. 정답은 {answer}입니다!')
elif user_answer > answer :
    print(f'계속 진행해보세요! 숫자가 너무 큽니다! {username}님')
elif user_answer < answer:
    print(f'계속 진행해보세요! 숫자가 너무 작습니다!{username}님')
else: 
    print(f'틀렸습니다! 정답은 {answer}입니다!')

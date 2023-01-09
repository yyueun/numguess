## Numguess 게임을 시작합니다.
---------------------------------
from random import randint


username= input("이름을 작성해주세요: ")
print(f"안녕하세요,{username}님! 1-100까지의 정수를 하나 맞춰주세요")


answer = random.randint(1,100)


user_answer = int(input("숫자를 입력해주세요 : ")
print(f'{username}님, 당신이 선택한 숫자는 {user_answer}입니다!')


print(f"정답은 {answer}이었습니다!")

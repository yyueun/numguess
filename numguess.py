from time import sleep
from random import randint
username= input("이름을 작성해주세요: ")
print(f"안녕하세요,{username}님! 1-100까지의 정수를 하나 맞춰주세요")


def user_input():
  try:
    user_answer = int(input("숫자를 입력해주세요 : "))
    return user_answer
  except:
    user_input()


def numguess(try_c = 10, answer = random.randint(1,100)):
  while True:
    if try_c == 0:
      print(f'틀렸습니다! 정답은 {answer}')
      break
    user_answer = user_input()

    if user_answer == answer:
      print(f'축하합니다. 정답은 {answer}입니다!')
    elif user_answer > answer :
      try_c -= 1
      print('계속 진행해보세요! 숫자가 너무 큽니다! ')
    else:
      try_c -= 1
      print('계속 진행해보세요! 숫자가 너무 작습니다!')






numguess()




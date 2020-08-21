# 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: "가 출력됩니다. 총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
# 정답을 맞추면 "축하합니다. *번 만에 숫자를 맞추셨습니다."가 출력되고 프로그램은 종료됩니다.
# 사용자가 입력한 수가 정답보다 작은 경우 "Up"이 출력되고, 입력한 수가 정답보다 큰 경우 "Down"이 출력됩니다.
# 정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞추지 못했으면, "아쉽습니다. 정답은 *입니다."가 출력되고 프로그램은 종료됩니다.

import random

answer = random.randint(1, 20)
count = 4

while True:
    if count == 0:
        print("아쉽습니다. 정답은 {}입니다.".format(answer))
        break
    n = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: ".format(count)))
    if n == answer:
        print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(5-count))
        break
    elif n < answer:
        print("UP")
    elif n > answer:
        print("DOWN")
    count -= 1

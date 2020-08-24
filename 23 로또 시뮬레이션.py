# 규칙
# 로또는 주 1회씩 열립니다. 하지만 한 사람이 한 회차에 여러 번 참여할 수도 있습니다.
# 번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.
# 당첨 액수는 아래 규칙에 따라 결정됩니다.
# 1. 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 2. 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 3. 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 4. 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 5. 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)


# 과제 설명
# 여러분의 임무는 로또 시뮬레이션을 위한 함수들을 작성하는 것입니다. 어떤 함수들이 있는지 봅시다.

# generate_numbers
# 이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다.
# 예를 들어서 print(generate_numbers(6)) 를 실행하면
# [16, 2, 30, 40, 15, 33] 이런 결과가 나올 수 있습니다. 하지만 다시 실행하면 다른 결과가 나오겠죠?
# 참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.

# draw_winning_numbers
# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
# 예를 들어서 print(draw_winning_numbers()) 를 실행하면
# [4, 12, 14, 28, 40, 41, 6] 이런 결과가 나올 수 있습니다.
# 앞서 정의한 generate_numbers 함수를 잘 활용하면, 함수를 간결하게 작성할 수 있습니다.

# count_matching_numbers
# 파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
# 예를 들어서 print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35])) 를 실행하면
# 2, 11, 13이 겹치기 때문에 3이 나옵니다.
# 또 print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14])) 를 실행하면,
# 14가 겹치기 때문에 1이 나오겠죠?

# check
# 참가자의 당첨 금액을 리턴합니다. 파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요.
# numbers는 당연히 번호 여섯 개를 담고 있고, winning_numbers는 보너스까지 해서 번호 7개를 담고 있겠죠?
# 예를 들어서 아래 코드를 실행하면,
#numbers_test = [2, 4, 11, 14, 25, 40]
#winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]
#print(check(numbers_list, winning_numbers_test))
# 4, 14, 40... 이렇게 번호 3개가 겹치기 때문에 5천 원에 당첨됩니다.

from random import randint


def generate_numbers(n):
    newlist = []
    while True:
        a = randint(1,45)
        if a in newlist:
            continue
        newlist.append(a)
        if len(newlist) == n:
            break
    return newlist
    
#def generate_numbers(n):
#    numbers = []
#    while len(numbers) < n:
#        num = randint(1, 45)
#        if num not in numbers:
#            numbers.append(num)
#    return numbers    


def draw_winning_numbers():
    newlist = generate_numbers(7)
    last = newlist.pop()
    newlist.sort()
    newlist.append(last)
    return newlist
    
#def draw_winning_numbers():
#    winning_numbers = generate_numbers(7)
#    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(list_1, list_2):
    count = 0
    for num in list_1:
        if num in list_2:
            count += 1
    return count

#def count_matching_numbers(numbers, winning_numbers):
#    count = 0
#    for num in numbers:
#        if num in winning_numbers:
#            count = count + 1
#    return count


def check(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers[:-1]:
            count += 1
    if count == 6 and winning_numbers[-1] in numbers:
        return 1000000000
    elif count == 5 and winning_numbers[-1] in numbers:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
        
#def check(numbers, winning_numbers):
#    count = count_matching_numbers(numbers, winning_numbers[:6])
#    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
#    if count == 6:
#        return 1000000000
#    elif count == 5 and bonus_count == 1:
#        return 50000000
#    elif count == 5:
#        return 1000000
#    elif count == 4:
#        return 50000
#    elif count == 3:
#        return 5000
#    else:
#        return 0 

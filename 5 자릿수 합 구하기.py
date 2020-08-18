# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    count = 0
    for n in str(num):
        count += int(n)
    return count

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
count_sum = 0
for i in range(1, 1001):
    count_sum += sum_digit(i)
print(count_sum)

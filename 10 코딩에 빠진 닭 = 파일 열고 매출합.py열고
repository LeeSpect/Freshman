# chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요. 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.


with open('data/chicken.txt', 'r') as f:
    chicken = []
    sum = 0
    for line in f:
        chicken.append(line.split()[-1])
    for num in chicken:
        sum += int(num)
    print(sum/len(chicken))
    
# with open('data/chicken.txt', 'r') as f:
#     total_revenue = 0
#     total_days = 0
    
#     for line in f:
#         data = line.strip().split(": ")
#         revenue = int(data[1])  # 그날의 매출

#         total_revenue += revenue
#         total_days += 1

#     print(total_revenue / total_days)    

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xe2 in position 6987: illegal multibyte sequence
# 파이선에서 파일을 읽을때 위와 같은 오류가 표시된다면,
# 아래와 같이 파일을 여세요.
# open('파일경로.txt', 'rt', encoding='UTF8')

with open('vocabulary.txt', 'rt', encoding='UTF8') as f:
    for line in f:
        ques = line.strip().split(': ')
        ans = input("{}: ".format(ques[1]))
        if ans == ques[0]:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(ques[1]))
        print()
        
# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]

        # 유저 입력값 받기
#         guess = input("{}: ".format(korean_word))
#         
        # 정답 확인하기
#         if guess == english_word:
#             print("정답입니다!\n")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))      

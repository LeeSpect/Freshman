# 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요. 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.
# 이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.
# 같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random

with open('vocabulary.txt', 'rt', encoding='UTF8') as f:
    linelist = []
    for line in f:
        linelist.append(line)
    while True:
        i = random.randint(0,len(linelist)-1)
        ques = linelist[i].strip().split(': ')
        ans = input("{}: ".format(ques[1]))
        if ans == "q":
            break
        elif ans == ques[0]:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(ques[1]))
        print()
        
# 우선 vocabulary.txt 파일을 읽고, 파이썬 사전을 채워 넣겠습니다.
#vocab = {}
#with open('vocabulary.txt', 'r') as f:
#    for line in f:
#        data = line.strip().split(": ")
#        english_word, korean_word = data[0], data[1]
#        vocab[english_word] = korean_word     
# 이렇게 하면 파일에 있는 단어와 뜻이 모두 vocab 사전에 정리되겠죠?

# 영어 단어 목록을 받아오려면 파이썬 사전의 keys를 사용하면 되는데요. 여기서 랜덤한 영어 단어를 뽑고 싶은 거죠.
# 1. random 모듈의 randint 함수를 이용해서 랜덤한 인덱스를 받는다.
# 2. 그 랜덤한 인덱스를 통해 vocab.keys() 리스트에서 단어를 받는다.
#keys = list(vocab.keys())
#index = random.randint(0, len(keys) - 1)
#english_word = keys[index]

# 그리고 이제 이에 해당하는 한국어 뜻을 받아오는 것은 너무 쉽습니다.
#korean_word = vocab[english_word]

# 나머지 부분은 앞선 실습 과제랑 거의 똑같습니다.
# 1. 유저에게 단어를 입력 받는다.
# 2. 만약 유저가 q를 입력했으면 프로그램을 종료한다.
# 3. 유저가 입력한 영어 단어가 정답인지 확인한다.


# 모범 답안
#import random

# 사전 만들기
#vocab = {}
#with open('vocabulary.txt', 'r') as f:
#    for line in f:
#        data = line.strip().split(": ")
#        english_word, korean_word = data[0], data[1]
#        vocab[english_word] = korean_word

# 문제 내기
#while True:
    # 랜덤한 문제 받아오기
#    keys = list(vocab.keys())
#    index = random.randint(0, len(keys) - 1)
#    english_word = keys[index]
#    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
#    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
#    if guess == 'q':
#        break
    
    # 정답 확인하기
#    if guess == english_word:
#        print("정답입니다!\n")
#    else:
#        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

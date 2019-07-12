# 사운드 모듈
import winsound
# 사운드재생
# winsound.PlaySound(사운드파일경로,winsound.SND_FILENAME)
#
# winsound.PlaySound('sound/good.wav',winsound.SND_FILENAME)
# winsound.PlaySound('sound/bad.wav',winsound.SND_FILENAME)

# ------------------>
# 1단계 : 사운드와 if
# 샘플 텍스트와 동일하게 입력하면
# 사운드 재생
# 메세지 출력
def q1():
    sample = 'python'
    print(sample)
    inData = input('단어 입력 : ..... ')
    if inData.strip() == sample:
        winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME)
        print(' Pass ')
    else:
        winsound.PlaySound('sound/bad.wav', winsound.SND_FILENAME)
        print(' Fail')

# ------------------>
# 2단계 : 리스트의 단어 섞기 - 랜덤 리스트
# 랜덤 단어가 중복이 되지 않아야 한다.
# 중복되지 않고 5개의 단어 표시
# random.shuffle(리스트)
# : 리스트를 무작위로 순서 재정렬. print 문과 바로 사용 불가
# 0~4개 추출

import random

# wordList = ['word','corail','banana',
#             'choice','print','python','append',
#             'insert','delete','computer']
#
# # num = random.randint(0,len(wordList)-1)
# # print(num)
# # print(wordList[num])
# # 문제점 : 중복
# # for i in range(0,3):
# #     num = random.randint(0,len(wordList)-1)
# #     print(wordList[num])
#
# # print(random.shuffle(wordList)) # None
#
# print('원본 : ', wordList)
# random.shuffle(wordList)
# print(wordList[0:5])

# ------------------>
# 3단계 : 맞는 갯수 카운팅
# wordList = ['word','corail','banana',
#             'choice','print','python','append',
#             'insert','delete','computer']
# random.shuffle(wordList)
# print(wordList)
# # 맞는 갯수 카운팅
# cnt = 0
# for i in range(0, 5):
#     # wordList[i] 는 문자열로 변경
#     sample = str(wordList[i])
#     print('\n',sample, '\n')
#     inData = input('단어 입력 : ..... ')
#     if inData.strip() == sample:
#         winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME)
#         print(' Pass ')
#         # 정답수 증가
#         cnt += 1
#     else:
#         winsound.PlaySound('sound/bad.wav', winsound.SND_FILENAME)
#         print(' Fail')
#
# print(' 정답 갯수 : ', cnt)

# ------------------------------------
def wordGame():
    wordList = ['word','corail','banana',
                'choice','print','python','append',
                'insert','delete','computer']
    random.shuffle(wordList)
    print(wordList)
    # 맞는 갯수 카운팅
    cnt = 0
    for i in range(0, 5):
        # wordList[i] 는 문자열로 변경
        sample = str(wordList[i])
        print('\n',sample, '\n')
        inData = input('단어 입력 : ..... ')
        if inData.strip() == sample:
            winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME)
            print(' Pass ')
            # 정답수 증가
            cnt += 1
        else:
            winsound.PlaySound('sound/bad.wav', winsound.SND_FILENAME)
            print(' Fail')

    print(' 정답 갯수 : ', cnt)

# ------------------------------------
# 4단계
# : 단어텍스트파일을 리스트화

with open('resource/word.txt','r') as f:
    # 한행씩 리스트로 변경
    wordList = f.readlines()
    # \n 가 단어마다 삽입되는지 확인?
    print(wordList[0:10])

    # \n 를 각 리스트 요소에서 삭제
    for i in range(0, len(wordList)-1):
        wordList[i] = wordList[i].replace('\n','')
    # \n 가 단어마다 삭제되었는지 확인
    print(wordList[0:10])

# ------------------------------------
# 5 단계
'''
Ready? Press Enter Key!!!!
게임시작 
...
게임종료 
...
정답수 : ?
( 추가 과정 =>
데이타베이스 생성 : id(int) / count(int) / date(text) 
아이디, 정답수, 오늘날짜 를 데이타에 저장
오늘날짜 생성 : datetime 모듈 이용 
) 

게임을 종료하시겠습니까?(y) ..... 

'''
import datetime
now = datetime.datetime.now()
# 오늘날짜, 현재시분초
print(now)
print(now.month)
print(now.hour)

input('Ready? Press Enter Key!!!!')
print(' ... ')













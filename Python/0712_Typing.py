import os
import random
import time

bad = "./data/typing/sound/bad.wav"
good = "./data/typing/sound/good.wav"

with open('./data/typing/resource/word.txt', 'r') as f:
    text = f.readlines()
    text = [word.strip() for word in text]
    cnt = 0

    start_time = time.time()
    while True:
        cnt += 1

        idx = random.randrange(0, len(text))

        print(text[idx])
        ans = input()

        if text[idx] == ans:
            print("Correct")
            os.system('aplay ' + good)
        else:
            print("Fail")
            os.system('aplay ' + bad)
            print(f'{cnt}, {(time.time() - start_time):.2f}s')
            break;

from string import ascii_lowercase, ascii_uppercase
def solution(word):
    answer = ''
    
    up = list(ascii_uppercase)
    upRvs = sorted(up, reverse=True)
    low = list(ascii_lowercase)
    lowRvs = sorted(low, reverse=True)


    for i in word:
        if (i>='A' and i<='Z'):
            cnt = 0
            for j in up:
                if i==j:
                    answer+=upRvs[cnt]
                cnt+=1
        elif (i>='a' and i<='z'):
            cnt = 0
            for j in low:
                if i==j:
                    answer+=lowRvs[cnt]
                cnt+=1
        else:
            answer+=i
    return answer

word = 'I love you'
print(solution(word))
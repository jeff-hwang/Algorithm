'''
def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x: len(x))
    
    pbLen = len(phone_book)
    if pbLen == 1:
        return answer
    for i in range(0, pbLen-1):
        ln = len(phone_book[i])
        for j in range(i+1, pbLen):
            if phone_book[i] == phone_book[j][0:ln]:
                answer = False
                break

    return answer 
'''
i = '123'
j = '12345'
print(j.find(i,len(i)))

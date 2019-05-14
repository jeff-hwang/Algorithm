def solution(phone_book):

    # phone_book을 원소의 길이를 기준으로
    # 오름차순으로 정렬
    phone_book.sort(key = lambda x: len(x))
    
    # 매개변수 배열의 크기를 구함
    pbLen = len(phone_book)
    
    # 2중 for 문을 사용하여 하나 하나 비교해본다.
    # 0 ~ pbLen-1
    for i in range(0, pbLen-1):
        # i 번째 인덱스의 길이를 k에 대입
        k = len(phone_book[i])
        # i+1 ~ pbLen 까지 for 문
        for j in range(i+1, pbLen):
            # j 번째 원소의 0~k-1 의 문자가 phone_book[i]
            # 와 같다면 return False
            if phone_book[i] == phone_book[j][0:k]:
                return False
    # 반복문을 무사히 통과하면 return True
    return True

if __name__ == "__main__":
    phone_book = ["911", "97625999", "91125426"]
    s = solution(phone_book)
    print(s)
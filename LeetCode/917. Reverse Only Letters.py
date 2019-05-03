class Solution(object):
    def reverseOnlyLetters(self, S):
        
        # 파라미터를 List로 변경
        listS = list(S)
        # 리스트의 길이
        ln = len(listS)

        # 알파벳 나온 것을 reverse한 정보
        swap = []
        # swap할 index 저장소
        index = []

        # 0 ~ ln-1 반복
        for i in range(ln):
            # listS 의 원소가 알파벳인지 확인
            if listS[i].isalpha() :
                # index에 i 위치 정보를 append
                index.append(i)
                # swap에 listS[i] 맨 앞으로 삽입
                swap.insert(0, listS[i])
        
        # index의 길이
        indexLen = len(index)

        # index 길이 만큼 반복
        for i in range(indexLen):
            # 해당 인덱스에 swap 정보를 대입
            listS[index[i]] = swap[i]      
        
        # listS의 원소들을 String 형태로 합쳐 return
        return "".join(listS)

if __name__ == "__main__":
    inData = "ab-cd"
    
    print(Solution().reverseOnlyLetters(inData))
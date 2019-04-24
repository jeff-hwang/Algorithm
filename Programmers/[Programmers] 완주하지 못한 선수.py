'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.


입출력 예
participant	completion	return
[leo, kiki, eden]	[eden, kiki]	leo
[marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
[mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav
'''

# 1차 풀이 # 효율성 20%
'''
def solution(participant, completion):
    answer = ''
    
    # 문제에서 제시한 조건 중 완주자는 항상 참가자의 수보다 한명 작다고 하였으므로
    # sorted funtion을 사용하여 문자순으로 오름차순 정렬을 할 수 있을 거라 생각
    # 매개 변수를 오름차순으로 정렬해준다.
    participant = sorted(participant)
    completion = sorted(completion)
    
    # compLen 은 완주자의 길이
    compLen = len(completion)

    # 참가자를 하나하나 오름차순으로 비교한다.
    for i in participant:
        # switch 는 반복문을 돌렸을 때 i와 j가 다르면 True로 변경시키려고 만듬
        switch = False
        
        # compLen 만큼 반복문을 돌려 i 와 완주자가 같으면 True
        for j in range(compLen):
            if i == completion[j]:
                # 완주자가 일치하면 pop
                completion.pop(j)
                switch = True
                # pop 을 하게 되면 완주자의 총길이가 줄으므로 -1 을 해준다.
                compLen -= 1
                break
        # False 이면 일치 하지 않은 것이므로 answer 에 i를 대입
        # 반복문을 빠져나감
        if switch == False:
            answer = i
            break
    return answer
    # 정답은 맞지만 효율성이 안 좋아 실패함
'''
# 2차 풀이
def solution(participant, completion):
    answer = ''
    # 동일하게 오름차순으로 매개변수 수정한다.
    participant = sorted(participant)
    completion = sorted(completion)
    
    compLen = len(completion)
    
    for i in range(compLen):
        # 참가자와 완주자의 i번째가 일치하지 않으면 answer에 참가자[i]를 대입
        if participant[i] != completion[i]:
            answer = participant[i]
            # return answer 시킨다.
            return answer
    
    # 반복문이 종료되었으면 남은 마지막 참가자가 완주하지 못한 것이므로
    # 참가자의 맨마지막을 return 한다.
    return participant[-1]
    


participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

sl = solution(participant, completion)
print(sl)
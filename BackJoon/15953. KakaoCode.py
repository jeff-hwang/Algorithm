class KakaoCode(object):
    # 경우의 수에 따른 상금을 저장해 놓은 stack 변수
    stack = []

    def __init__(self):
        # 대회 1의 상금 정보와 인원 수
        self.test1 = [
            {'rank' : 1, 'prize': 500, 'amount':1},
            {'rank' : 2, 'prize': 300, 'amount':2},
            {'rank' : 3, 'prize': 200, 'amount':3},
            {'rank' : 4, 'prize': 50, 'amount':4},
            {'rank' : 5, 'prize': 30, 'amount':5},
            {'rank' : 6, 'prize': 10, 'amount':6}
        ]
        # 대회 2의 상금 정보와 인원 수
        self.test2 = [
            {'rank' : 1, 'prize': 512, 'amount':1},
            {'rank' : 2, 'prize': 256, 'amount':2},
            {'rank' : 3, 'prize': 128, 'amount':4},
            {'rank' : 4, 'prize': 64, 'amount':8},
            {'rank' : 5, 'prize': 32, 'amount':16}
        ]

    # 획득 할 수 있는 상금을 저장    
    def printPrizes(self, data):
        # 빈 칸을 기준으로 1차 2차 등수를 매김
        data = list(map(int, data.split(' ')))
        
        # 대회1의 순위
        rankTest1 = 0
        # 대회2의 순위
        rankTest2 = 0
        # 총 상금 정보
        prize = 0

        # 예외 체크 : 등수가 0이 아니라면 정상적인 상금
        if data[0] != 0:
            # 대회 1의 상금 인원을 체크하기 위한 반복문
            for i in self.test1:
                # 인원을 더한다.
                rankTest1+=i['amount']
                # 자신의 등수가 랭크에 속하면 총상금에 prize를 더한다.
                if rankTest1>=data[0]:
                    prize+=i['prize']
                    break
                # 순위에 들지 못하면 상금은 0을 더한다.
                else:
                    prize+=0
        # 등수가 0이라면 상금이 없다. -> testcase 참 이상하게 .... 0등이 어딨어...
        else:
            prize+=0
        
        # 대회 2의 case.. 대회 1의 경우와 같은 방식으로 check한다.
        if data[1] != 0:
            for i in self.test2:
                rankTest2+=i['amount']
                if rankTest2>=data[1]:
                    prize+=i['prize']
                    break
                else:
                    prize+=0
        else:
            prize+=0
        
        # stack 에 상금 정보를 추가
        self.stack.append(prize*10000)
        


if __name__=="__main__":
    # 경우의 수
    N = int(input())
    kakao = KakaoCode()
    
    for i in range(N):
        kakao.printPrizes(input())

    for i in kakao.stack:
        print(i)
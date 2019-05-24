class Simulator(object):
    def __init__(self, time, chef, waiter, tableCnt):
        self.time = time # 시간
        self.chef = chef # 요리사
        self.waiter = waiter
        self.tableCnt = tableCnt
        self.emptyTab = [{'outTime' : 0, 'cleanTime' : 3 } for i in range(tableCnt)] # 빈 테이블
        self.usingTab = [] # 사용 중 테이블
        self.waitTab = []
        self.guest = []
    
    def crtGuest(self): # 손님 생성
        self.guest.append({'lmTime' : 6, 'cnt' : 7 }) # 최대 대기시간 60분, 인원 7명
        if self.guest[0]['lmTime'] == 0 : # 최대 대기시간을 넘기면 손님이 나감
            self.guest.pop(0)

    def respGuest(self): # 손님 응대
        if self.waitTab != None:
            while True:
                if self.waitTab[0]['cleanTime'] == 0:
                    self.emptyTab.append(self.waitTab.pop(0))
                else :
                    break
                
        while True:
            if self.emptyTab != None and self.chef != None \
                and self.guest != None : # 테이블이 존재하고, 요리사와 손님이 있으면 손님 응대
                cache = self.emptyTab.pop(0) # 비어있는 테이블의 임시저장 변수
                cache['outTime'] = 15 # outTime을 15분 뒤로 설정
                self.usingTab.append(cache) # 사용 중인 테이블에 추가
                self.guest[0]['cnt'] -= 1
                if self.guest[0]['cnt'] == 0:
                    self.guest.pop(0)
            else :
                break

    def cleanTable(self): # 청소
        if self.waitTab != None and self.waiter != 0:
            for i in range(self.waiter):


            
            
    
    
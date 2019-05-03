# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

def calcTwoNum(A, B):
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)

if __name__ == "__main__":
    a = [ int(i) for i in input().split(' ') ]
    calcTwoNum(a[0],a[1])



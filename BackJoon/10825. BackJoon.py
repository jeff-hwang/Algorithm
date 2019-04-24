"""
*** 문제 설명  ***
input Data로 첫 번째 줄에는 학생들의 수를 받는 Integer를 받는다
학생 수 만큼 줄을 입력을 받는데 ' ' 빈 칸으로 데이터를 나눠서 학생의 정보를 등록을 하는데
첫 번째는 학생이름, 그 다음은 국어점수, 영어점수, 수학점수를 나타낸다.

출력은 학생의 성적 순으로 한 칸씩 출력 되게하는데
우선순위는 국어 점수 순으로 Desc(내림차순),
국어점수가 같으면 영어점수 Asc(오름차순),
영어점수도 같으면 수학점수 Desc,
모두 같다면 이름 순으로 나타낸다.

이번 문제는 클래스 형식으로 푼다.
"""
class ClassRoom(object):
    
    # 학생정보를 가질 list 변수
    students = []

    # 생성자
    def __init__(self, count):
        # 학생 수를 입력을 받아 저장할 변수
        self.count = count
        
        # 학생 리스트를 초기화 해준다.
        self.students = []

    # 학생의 정보를 입력을 받아 하나 하나 등록할 Method
    # 파라미터를 data는 이름 국어 영어 수학 점수를 가지고 있는 String Data
    def insertScore(self, data):
        # data를 빈칸으로 나누어 list로 저장한다.
        data = data.split(" ")

        # 학생 정보를 딕셔너리로 저장하려고 만든 변수
        student = {}
        # 학생 이름 정보
        student["name"] = data[0]
        # 국어 점수
        student["kor"] = int(data[1])
        # 영어 점수
        student["eng"] = int(data[2])
        # 수학 점수
        student["math"] = int(data[3])
        # 학생 리스트에 딕셔너리 정보를 append 한다
        self.students.append(student)

    # method overloading
    # BubbleSort Method -> O(n^2) : 느리다.
    def bubbleSort(self, students, last=None):
        # Method overloading
        # last 값이 없으면 last 는 학생의 길이로 대입한다.
        if last==None:
            self.bubbleSort(students, len(students))
        # last 값이 있으면 실행하는 부분
        else:
            # last 값이 0 보다 크면
            if (last > 0):

                for i in range(1, last):
                    # 국어 점수가 감소하는 순서로 swap
                    if students[i]["kor"]>students[i-1]["kor"]:
                        self.swap(students, i, i-1)

                    # 국어 점수가 같으면 영어 점수가 증가하는 순서로
                    elif students[i]["kor"]==students[i-1]["kor"]:
                        if students[i]["eng"] < students[i-1]["eng"]:
                            self.swap(students, i, i-1)

                        # 영어 점수가 같으면 수학 점수가 감소하는 순서로
                        elif students[i]["eng"] == students[i-1]["eng"]:
                            if students[i]["math"] > students[i-1]["math"]:
                                self.swap(students, i, i-1)
                            # 수학 점수가 같으면 이름 사전 순으로 증가
                            elif students[i]["math"] == students[i-1]["math"]:
                                if students[i]['name'] < students[i-1]["name"]:
                                    self.swap(students, i, i-1)
                    else :
                        pass
                self.bubbleSort(students, last-1)

    # swap 함수
    def swap(self, students, start, end):
        temp = students[start]
        students[start] = students[end]
        students[end] = temp  

    # 간단하게 lambda로 해서 우선 순위를 선정해 sorting 을 할 수 있다.
    def sortStudent(self, students):
        # 국어점수 desc, 영어점수 asc, 수학점수 desc, 이름 순 asc
        students.sort(key = lambda x: (100-x["kor"], x["eng"], 100-x["math"], x["name"]))
        

if __name__ == "__main__":
    classRoom = ClassRoom(int(input()))
    for i in range(classRoom.count):
        classRoom.insertScore(input())
    
    # Bubble Sort 로 할 경우 시간 초과가 발생하기 때문에 실패
    # classRoom.bubbleSort(classRoom.students)
    classRoom.sortStudent(classRoom.students)

    for i in classRoom.students:
        print(i["name"])

    
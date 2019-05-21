class StaticVar(object):
    def __init__(self, target):
        self.target = target
        self.cnt = 0

sv = None
def solution(numbers, target):
    global sv
    sv = StaticVar(target)
    targetDFS(numbers, 0)
    return sv.cnt
    

def targetDFS(numbers, index):
    if index < len(numbers):
        numbers[index] *= 1        
        targetDFS(numbers, index+1)

        numbers[index] *= -1
        targetDFS(numbers, index+1)
    elif sum(numbers) == sv.target:
        sv.cnt+=1

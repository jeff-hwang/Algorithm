def solution(lands, point, wells):
    answer = True
    if False in cmpLands(lands, wells):
        return False
    if True in pointLands(point, wells):
        return True
    else:
        return False


def cmpLands(lands, wells):
    lst = []
    for i in lands:
        if (i[0]<=wells[0] and i[2]>=wells[0]) \
            and (i[0]<=wells[2] and i[2]>=wells[2]) \
            and (i[1]<=wells[1] and i[3]>=wells[1]) \
            and (i[1]<=wells[3] and i[3]>=wells[3]):
            lst.append(False)

    return lst      
            
def pointLands(point, wells):
    lst = []
    for i in point:
        if (i[0]>=wells[0] and i[0]<=wells[3]) \
            and (i[3]>=wells[0] and i[3]<=wells[3]) \
            and (i[1]>=wells[1] and i[1]<=wells[3]) \
            and (i[3]>=wells[1] and i[3]<=wells[3]):
            lst.append(True)

    return lst


lands = [[10,0,30,5], [0,30,20,50],[30,30,40,40]]
wells = [[15,15,25,25],[40,10,50,20]]
point =[10,10,30,30]

print(solution(lands,wells, point))

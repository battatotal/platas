from sys import argv
import math



with open(argv[1], encoding='UTF-8') as file:
    mid = list(map(float, file.readlines(1)[0].replace("\n", "").split()))
    rad = float(file.readlines(2)[0].replace("\n", ""))


    
with open(argv[2], encoding='UTF-8') as file:
    points = [x.split() for x in file.readlines()]
    if len(points) < 101 or len(points) != 0:
        for i in points:
            for j in range(len(i)):
                i[j] = float(i[j])



def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def in_circle(point):
    if rad == distance(mid, point): return 0
    elif rad > distance(mid, point): return 1
    else: return 2

for i in range(len(points)):
    print(in_circle(points[i]))

    
    
    

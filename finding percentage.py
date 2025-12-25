

"""



"""



"""
from dictionary, take a custom name as input and then give 
average from the list of values

but the problem is that we need it upto 2 decimals
so instead of 10.0, we need 10.00
formatting comes into play

for floating point formatting, 

"%.3f" % 22/7

this will format 3.142857142... to 3 floating places
i.e., 3.143


"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

def averageCalc(dataDict, name):

    sum = 0
    for i in dataDict[name]:
        sum += i
    return "%.2f" % (sum / len(dataDict[name]))
        
    
print(averageCalc(student_marks, query_name))








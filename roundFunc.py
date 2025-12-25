


def main():

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(averageCalc(student_marks, query_name))

    #print(student_marks, type(student_marks), sep="\n\n")



def averageCalc(dataDict, name):

    sum = 0
    for i in dataDict[name]:
        sum += i
    return (sum / len(dataDict[name]))



main()
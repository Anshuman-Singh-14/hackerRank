



'''5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39'''

def secondLastBest():
    n = int(input())
    records = []

    for _ in range(n):
        name = input()
        score = float(input())
        
        records.append([name, score])

    # Create a set of unique scores, then convert to list and sort it
    unique_scores = sorted(set(score for name, score in records))
    second_lowest_score = unique_scores[1] # Takes the second lowest score

    # Create a list of name with second lowest score, then sort it
    names = [name for name, score in records if score == second_lowest_score]
    names.sort()

    for name in names:
        print(name)


def secondLastList():
    
    l=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    lscore = []
    
    for i in l:
        lscore.append(i[1])
    lscore.sort()
    secondlast = lscore[1]
    
    finallist = []
    for j in l:
        if j[1] == secondlast:
            finallist.append(j[0])
    finallist.sort()
    for k in finallist:
        print(k)




def secondLastDict():
    l=[]
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, "%.20f" % score])
        d["%.20f" % score] = []

    for i in l:
        d[i[1]].append(i[0])

    x = float(sorted(d.keys())[1])

    lx = []
    
    for m in d["%.20f" % x]:
        lx.append(m)
    lx.sort()
    for n in lx:
        print(n)

secondLastDict()
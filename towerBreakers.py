
#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    #

    moveFlag = 1
    # mf > 0 => p1 turn
    # mf < 0 => p2 turn

    validMoveFlag = True

    # check vmf 
    # if vmf is false, then check mf
    #           if mf > 0 then p2 wins
    #           if mf < 0 then p1 wins

    
    l = [m for i in range(n)]
    while validMoveFlag:
        # print(l)
        vm, validMoveFlag = findValidMove(l)
        res = checkWinner(moveFlag, validMoveFlag)
        if validMoveFlag:
            l, moveFlag = makeMove(l, vm, moveFlag)
        else:
            return res

def checkWinner(mf, vmf):

    if vmf == False:

        if mf == 1:
            return 2
        elif mf == -1:
            return 1

    else:
        pass


def findValidMove(l):

    move = []
    vmf = False

    for i in range(len(l)):
        
        if l[i] > 1:
            # print("found > 1")
            vmf = True

            for j in range(l[i], 1, -1):
                # print(j)
                # print(l[i], j, )
                if l[i] % j == 0:
                    move = [i, j]
                    # print(move)
                    break
            break
        else:
            pass
            # print("didnt find")
    return move, vmf
    

def makeMove(l, move, mf):

    l[move[0]] = l[move[0]] // move[1]
    mf *= -1

    return l, mf


def main():
    res = []
    for _ in range(int(input())):

        dataIn = input().rstrip().split()
        
        n = dataIn[0]   # number of towers
        m = dataIn[1]   # height of each tower

        res.append(towerBreakers(int(n), int(m)))
    print(*(k for k in res), sep="\n")
main()


"""



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

"""
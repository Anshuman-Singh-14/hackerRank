
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

    vm, validMoveFlag = checkValidMove(l)

    #print(l)


def checkValidMove(l):

    move = []
    vmf = True



    return move, vmf
    

def main():

    for _ in range(int(input())):

        dataIn = input().rstrip.split()
        
        n = dataIn[0]   # number of towers
        m = dataIn[1]   # height of each tower

        towerBreakers(n, m)
        
towerBreakers(4, 4)



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
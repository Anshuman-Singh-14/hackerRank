


#import textwrap

def wrap(string, max_width):
    c = int(max_width)
    strx = string.strip()
    n = 0
    out = str()
    while n < len(strx)-c:
        out += strx[n:n+c] + '\n'
        n += c
    out += strx[n:]
    return out

if __name__ == '__main__':
    #string = input().strip()
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width =  int(input())
    result = wrap(string, max_width)
    print(result)
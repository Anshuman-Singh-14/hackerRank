

'''
required output for int input 17

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

----1 ---1 ---11 ----1
----2 ---2 ---11 ---10
----3 ---3 ---11 ---11
----4 ---4 ---11 --100
----5 ---5 ---11 --101
----6 ---6 ---11 --110
----7 ---7 ---11 --111
----8 ---10 ---11 -1000
----9 ---11 ---11 -1001
---10 ---12 ---11 -1010
---11 ---13 ---11 -1011
---12 ---14 ---11 -1100
---13 ---15 ---11 -1101
---14 ---16 ---11 -1110
---15 ---17 ---11 -1111
---16 ---20 ---11 10000
---17 ---21 ---11 10001
'''



def print_formatted(number):
    # your code goes here

    binary = bin(number)[2:]
    octal = oct(number)[2:]
    hexa = hex(number)[2:].upper()
    
    wdth = len(binary)
    for i in range(1, number + 1):
        
        print("-"*( len( bin(number)[2:])  -  len(bin(i)[2:]) ),i, sep='', end=' ')
        print("-"*( len( bin(number)[2:])  -  len(bin(i)[2:]) ), oct(i)[2:], sep='', end=' ')
        print("-"*( len( bin(number)[2:])  -  len(bin(i)[2:]) ), hex(number)[2:].upper(), sep='', end=' ')
        print( "-"*(len( bin(number)[2:])  -  len(bin(i)[2:]) ) , bin(i)[2:], sep='', end='\n')
    # 
    # print(length)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# str(hex(142)[2:]).upper() 

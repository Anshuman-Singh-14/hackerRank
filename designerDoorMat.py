


"""


output for 9 and 27

m = 27
n = 9
m horizontally and n vertically
m is odd, n is 3*n

d = ".|."


--- --- --- --- .|. --- --- --- ---
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------



"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

n = int(n) #9 vertically rows.
m = int(m) #27 horizontally columns .

d = ".|."
welcome = "WELCOME"


#top half
#(n-1)/2 iterations
"""

divide by 3 for each row

"""






for i in range(0, n // 2):
    print(((n//2)-i)*'---' + d*(2*i+1) + ((n//2)-i)*'---')



print(welcome.center(3*n, "-"))


for i in range((n // 2)-1, -1, -1):


    print(((n//2)-i)*'---' + d*((2*i)+1) + ((n//2)-i)*'---')



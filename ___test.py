n = 9 #9 vertically rows.
m = 27 #27 horizontally columns .

d = ".|."
welcome = "WELCOME"

'''
((n//2)-i)*'---'
--- --- --- --- .|. --- --- --- ---

'''

for i in range(n // 2):
    print(((n//2)-i)*'---' + d*(2*i+1) + ((n//2)-i)*'---')



print(welcome.center(3*n, "-"))


for i in range(n // 2, -1, -1):
    print(((n//2)-i)*'---' + d*(2*i+1) + ((n//2)-i)*'---')
















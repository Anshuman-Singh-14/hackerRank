n = int(input())
l = [int(x) for x in input().split()]

print(l, type(l))
t = tuple(l)

print(hash(t))
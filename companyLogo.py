
# string input of name

"""

get a frequency breakdown of the characters in the string s
sort them in a descending order
for 2 characters having the same frequency, sort them alphabetically


"""

def main():

    s = input()

    d = {}
    for i in s:
        d[i] = 0
    for j in s:
        d[j] += 1

    print(d)
    l = list()

    for k in d:
        l.append([k, d[k]])

    print(l)

main()

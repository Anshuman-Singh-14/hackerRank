

# 1 w 2 r 3g
# 1 W 2 R 3g


# def solve(s):
#     return s.title()
"""
so apparently the title() method does not work as expected 
for the last term, 3g, it capitalises g to G.
if we try "14114135153a".title() it returns "14114135153A"
"""


def solve(s):
    words = s.split(' ')
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)

print(solve(input()))


# if __name__ == '__main__':
#     fptr = open(os.environ['C:/Users/admin/Documents/GitHub/leetcode/new.txt'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()

def count_substring(string, sub_string):

    counter = 0
    ct = 0
    string = "".join(string.split())
    sub_string = "".join(sub_string.split())
    listMain = list(string)
    listSub = list(sub_string)
    #print(listMain)
    #print(listSub)
    for i in range(len(listMain)):
        if listMain[i] == listSub[0]:
            for j in range(len(listSub)):
                if i+j < len(listMain) and listMain[i+j] == listSub[j]:
                    print("\n\n", i, j, i+j, listMain[i+j], listSub[j]  )
                    #print(listMain[i+j], listSub[j])
                    ct+=1
                    if ct == len(listSub):
                        counter += 1
                        ct = 0
        
    """
    14 - l
    15 - d
    16 - ,

    """
    return counter

#if __name__ == '__main__':
string = "In the convential world, it won't ever happen".strip()
sub_string = "lD,".strip()

count = count_substring(string, sub_string)
print(count)
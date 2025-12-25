


def average(array):

    l = set(array)
    return (sum(l)/len(l))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
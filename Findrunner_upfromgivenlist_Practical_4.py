if __name__=="__main__":
    n = int(input())
    a = map(int, input().split())
    a = list(set(list(a)))
    temp = len(a)
    a = sorted(a)
    print(a[temp-2])
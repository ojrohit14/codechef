for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ""
    for i in range(0,n,4):
        curr = int(s[i:i+4],2) + 97
        res += chr(curr)
    print(res)
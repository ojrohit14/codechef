t = int(input())
for _ in range(t):
    res = None
    N,K,D = [int(x) for x in input().split(" ")]      #1 2 3 -> N=1 K=2 D=3
    a = [int(x) for x in input().split()]
    total_problems = sum(a) if K*D > sum(a) else K*D
    if total_problems < K:
        res = 0
    else:
        res = total_problems // K
    print(res)

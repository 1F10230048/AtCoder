N = int(input())
A = list(map(int, input().split()))
answer = False
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and k != i and i < j and j < k:
                if A[i] + A[j] + A[k] == 1000:
                    answer = True
                    break
if answer:
    print("Yes")
else:
    print("No")

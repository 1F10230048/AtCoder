N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = False
for i in range(N):
    if A[i] == X:
        answer = True
if answer == True:
    print("Yes")
else:
    print("No")

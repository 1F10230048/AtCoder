A, B = map(int, input().split())
answer = False
for i in range(A, B + 1):
    if 100 % i == 0:
        answer = True
if answer == True:
    print("Yes")
else:
    print("No")

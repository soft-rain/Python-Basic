n = int(input())
a = input().split()

arr = []

for i in range(n):
    arr.append(int(a[i]))

for i in reversed(range(n)):
    print(arr[i], end=" ")


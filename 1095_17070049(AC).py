n = int(input())
a = input().split()

arr = []

for i in range(n):
    arr.append(int(a[i]))

arr = sorted(arr)
print(arr[0])

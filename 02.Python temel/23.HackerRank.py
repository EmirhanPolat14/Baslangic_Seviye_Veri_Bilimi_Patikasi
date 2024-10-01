n = int(input())  
arr = map(int, input().split())

arr = list(set(arr))[-2]
print(arr)
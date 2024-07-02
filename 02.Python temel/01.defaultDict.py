from collections import defaultdict

a, b= map(int, input().split(" "))
d = defaultdict(list)
for i in range(a):
    d["A"].append(input())


for j in range(b):
    l = input()
    for indeks, eleman in enumerate(d["A"]):
        if l == eleman:
            print(indeks+1, end=" ")
        elif l not in d["A"]:
            print(-1)
    print(" ")

        


        




        
        


# print("a" in d["A"])
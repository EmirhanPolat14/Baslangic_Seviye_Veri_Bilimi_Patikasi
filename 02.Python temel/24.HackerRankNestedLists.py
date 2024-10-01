records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
    records=sorted(records)

scores = []
for i in range(len(records)):
    scores.append(records[i][1])
    scores.sort()


for i,j in records:
    if scores[1] == j:
        print(i)




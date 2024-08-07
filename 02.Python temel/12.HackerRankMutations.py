def mutate_string(string, position, character):
    new = ""
    for j,i in enumerate(string):
        if j == position:
            i = character
        new += i
    return new
    


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
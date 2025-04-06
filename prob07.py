with open("input.txt","r") as f:
    file = f.read().strip()
    #file = file.split()

#file = "1678684123456789"
dicti = {}
for num in "0123456789":
    dicti[num] = -1

for num in file:
    dicti[num]+=1

mini = []
for thing in dicti.values():
    if thing == -1:
        mini.append(100000000000)
        continue
    mini.append(thing)

#print(mini)

print(f"{mini.index(min(mini))}: {min(mini)}")
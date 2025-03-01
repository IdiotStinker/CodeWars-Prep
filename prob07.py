with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split()

dicti = {}
for num in "124567890":
    dicti[num] = -1

for num in file:
    dicti[num]+=1


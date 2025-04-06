import math
with open("input.txt","r") as f:
    file = int(f.read().strip())
    #file = file.split()

check = []
for i in range(file):
    if i**2 > file:
        break
    if math.sqrt(file-i**2) == int(math.sqrt(file-i**2)):
        check.append([i, int(math.sqrt(file-i**2))])

maxi = []
for w, l in check:
    if not w*l in maxi:
        maxi.append(w*l)
#
#print(maxi)
if len(maxi) == 0:
    print("That diagonal does not lead to integer sides!")
else:
    final = check[maxi.index(max(maxi))]

    print(final[0], final[1])
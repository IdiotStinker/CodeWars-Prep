with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")

headMax = file[0]
midMax = file[1]
bottomMax = file[2]

L = len(file[4])

lineList = []
for l, line in file:
    lineList.append(0)
    for space in line:
        if space == " ":
            lineList[l] += 1
headlist = []
midlist = []
bottomlist = []
for num in lineList:
    if num == 0:
        continue
    elif num <= headMax:
        headlist.append(num)
    elif num <= midMax:
        midlist.append(num)
    elif num <= bottomMax:
        bottomlist.append(num)
bottomlist.sort()
headlist.sort()
midlist.sort()

headfinallist = []
for i in range(100):
    headfinallist.append("")

for h, head in enumerate(headlist):
    if h == 0:
        prev = head
        headfinallist[l] = head

        continue
    if head == prev:
        headfinallist[100-h] = head
        continue
    elif head == headMax:
        headfinallist[l] = head
        break

for head in 
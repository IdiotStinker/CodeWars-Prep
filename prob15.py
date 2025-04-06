with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")
num = file[0]
beans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
add = []
addstr = ""
sub = []
substr = ""
check = 0
v = True
maj = 0
amt = 0
for i in range(len(num)):
    beans[int(num[i])] = beans[int(num[i])]+1
for i in range(10):
    if beans[i] > amt:
        maj = i
target = str(maj) * len(num)
for i in range(len(num)):
    add.append(0)
    sub.append(0)
for i in range(len(num)):
    if int(num[i]) > int(target[i]):
        sub[i] = int(num[i]) - int(target[i])
    else:
        add[i] = int(target[i]) - int(num[i])
for i in range(len(num)):
    check = check + add[i]-sub[i]
    if check < 0:
        v = False
if check != 0:
    v = False
for i in range(add):
    addstr = addstr + str(add[i])
    substr = substr + str(add[i])
if v == True:
    s = "SUBTRACTED"
    a = "ADDED"
    t = "FINAL"
else:
    s = "AVAILABLE"
    a = "NEEDED"
    t = "IMPOSSIBLE"
print(f"{num} ORIGINAL")
print(f"{substr} {s}")
print(f"{addstr} {a}")
print(f"{target} {t}")
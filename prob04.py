with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split()
name = file[0].split(" ")[0]
file.pop(0)
s = 0
h = 0
t = 0
for i in range(len(file)):
    amts = file(i).split(" ")
    s = s + amts[0]
    h = h + amts[1]
    t = t + amts[2]
if s != 1:
    sp = "s"
else:
    sp = ""
if h != 1:
    sh = "s"
else:
    sh = ""
if t != 1:
    st = "s"
else:
    st = ""
amt = 13*s + 9*h + 2*t
print(f"{name} spent ${amt} on {s} shirt{sp}, {h} hat{sh}, and {t} sticker{st}.")
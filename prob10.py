with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("/n")
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
down = "abcdefghijklmnopqrstuvwxyz"
outp = ""
file.pop()
for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] in up:
            outp = outp + file[i][j].lower()
        elif file[i][j] in down:
            outp = outp + file[i][j].upper()
        else:
            outp = outp + file[i][j]
    outp = outp + "\n"
print(outp)
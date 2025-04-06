with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")
fg = file[0].split(" ")
acr = ""
for i in range(len(fg)):
    letter = fg[i][0]
    acr = acr + letter
print(acr)
with open("input.txt","r") as f:
    file = f.read().strip()
str1 = ""
str2 = ""
for i in range(len(file)):
    if i % 3 == 2:
        str2 = str2 + file[i]
    else:
        str1 = str1 + file[i]
print(str1)
print(str2)
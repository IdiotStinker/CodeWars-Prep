with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split()
ct = 0
for i in range(len(file[0])):
    if file[0][i].lower() == file[1].lower():
        ct = ct + 1
        
print(f"There are {ct} {file[1].upper}'s in {file[0]}")
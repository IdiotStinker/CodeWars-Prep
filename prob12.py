with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split()


if file[0] == "1" and file[1] == "1":
    print("1 1")
elif file[2] == "1":
    print("0 1")
else:
    print("0 0")
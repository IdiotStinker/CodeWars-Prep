with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")
file.pop()
print("{")
for i in range(len(file)):
    first = file[i].split(" = ")[0]
    second = file[i].split(" = ")[1]
    if i != len(file)-1:
        comma = ","
    else:
        comma = ""
    print(f"    \"{first}\":\"{second}\"{comma}")
print("}")
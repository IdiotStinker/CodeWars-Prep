import math

with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")
file.pop()
for i in range(len(file)):
    num1 = int(file[i].split(" ")[0])
    num2 = int(file[i].split(" ")[1])
    g = math.gcd(num1, num2)
    if num1 / num2 == num1 // num2:
        print(num1 // num2)
    else:
        if num1 < num2:
            print(f"{num1 // g}/{num2 // g}")
        else:
            num1n = num1 - (num1 // num2) * num2
            g = math.gcd(num1n, num2)
            print(f"{num1 // num2} {num1n//g}/{num2//g}")
with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")
import math
num = int(file[0].split()[0])

if file[0].split()[1] == "m":
    end = num*39.37008/12/5280
if file[0].split()[1] == "y":
    end = num*3/5280
if file[0].split()[1] == "ft":
    end = num/5280
if file[0].split()[1] == "in":
    end = num/12/5280

end = end / (int(file[1])/3600)

end = math.trunc(end*100)/100

print(end, "miles/hour")
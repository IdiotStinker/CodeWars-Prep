with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split(",")

for n, num in enumerate(file):
    if n+2 == len(file):
        break
    if n==0:
        ratio = int(file[1]) / int(file[0])
        dif = int(file[1]) - int(file[0])
    else:
        if not ratio == int(file[n+1]) / int(file[n]):
            ratio = False
        if not dif == int(file[n+1]) - int(file[n]):
            dif = False

if not ratio == False:
    if ratio > 1:
        final = "*"+str(int(ratio))
    else:
        final = "/"+str(int(1/ratio))
    
    print(f"Sequence: {final}")
    print(f"Next: {int(int(file[len(file)-1]) * ratio)}")

elif not dif == False:
    if dif > 0:
        final = "+"+str(dif)
    else:
        final = ""+str(dif)
    
    print(f"Sequence: {final}")
    print(f"Next: {int(file[len(file)-1]) + dif}")

else:
    print("Sequence: UNKNOWN")
    print("Next: UNKNOWN")
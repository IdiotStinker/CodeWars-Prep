with open("input.txt","r") as f:
    file = f.read()
    file=file.split("\n")
x=0
for line in file:
    x=x+1
x=x-2
if x!=1:
    print("Hey, ChatGPT, I need",x,"codes!")
else:
    print("Hey, ChatGPT, I need a code!")
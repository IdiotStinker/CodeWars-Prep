with open("input.txt","r") as f:
    file = f.read().strip()
    file = file.split("\n")

emailsFinal = []

for line in file:
    if line == ";;;":
        break
    l = line.split()
    #print(l)
    for emails in l:
        emails=emails.split(",")
        #print(emails)
        for email in emails:
            
            if not email.lower() in emailsFinal:
                emailsFinal.append(email.lower())

emailsFinal.sort()

for thing in emailsFinal:
    print(f"{thing};")


ahsoka@jedi.republic.gov;
ahsoka@republic.com;
anakin.spam@republic.com;
anakin@501st.republic.mil;
cmdr.bow@501st.republic.mil;
cmdr.cody@212nd.republic.mil;
cmdr.tano@501st.republic.mil;
cmdr.vill@501st.republic.mil;
cmdr.voca@501st.republic.mil;
cptn.gregor@212nd.republic.mil;
cptn.rex@501st.republic.mil;
leia@alderaan.void;
leia@imperial.senate.gov;
leia@republic.senate.gov;
lord.vader@501st.imperial.mil;
lt.waxer@212nd.republic.mil;
obiwan@unspellable.name;
padme@disney.co.uk;
padme@republic.senate.gov;
sgt.boomer@501st.republic.mil;
sgt.fox@501st.republic.mil;


ahsoka@jedi.republic.gov;
ahsoka@republic.com;
anakin.spam@republic.com;
anakin@501st.republic.mil;
cmdr.bow@501st.republic.mil;
cmdr.cody@212nd.republic.mil;
cmdr.tano@501st.republic.mil;
cmdr.vill@501st.republic.mil;
cmdr.voca@501st.republic.mil;
cptn.gregor@212nd.republic.mil;
cptn.rex@501st.republic.mil;
leia@alderaan.void;
leia@imperial.senate.gov;
leia@republic.senate.gov;
lord.vader@501st.imperial.mil;
lt.waxer@212nd.republic.mil;
obiwan@unspellable.name;
padme@disney.co.uk;
padme@republic.senate.gov;
sgt.boomer@501st.republic.mil;
sgt.fox@501st.republic.mil;
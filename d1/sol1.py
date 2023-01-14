f = open("p1.txt","r")
lines = f.readlines()

current = 0
max_cal = 0
for l in lines:
    if (l != '\n'):
        current += int(l)
    else:
        max_cal = max(current, max_cal)
        current = 0
print(max_cal) 



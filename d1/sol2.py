f = open("p1.txt","r")
lines = f.readlines()

elves_list = []
current = 0
for l in lines:
    if (l != '\n'):
        current += int(l)
    else:
       elves_list.append(current)
       current = 0
elves_list.append(current)
elves_list.sort(reverse=True)
print(sum(elves_list[0:3])) 
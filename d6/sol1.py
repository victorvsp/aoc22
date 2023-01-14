with open("p1.txt","r") as f:
    for l in f:
        i = 0
        while len(set(l[i:i+4])) < 4:
            i += 1
        print(i + 4)
        
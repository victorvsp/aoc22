
contains_count = 0
stacks = None
move_phase = False
with open("p1.txt","r") as f:
    it_l = iter(f)
    for l in it_l:

        if move_phase:
            l_list = l.split()
            print(l_list)
            n_boxes = int(l_list[1])
            origin_idx = int(l_list[3]) -1
            dest_idx = int(l_list[5]) -1

            s_og = stacks[origin_idx]
            stacks[dest_idx].extend(s_og[len(s_og)-n_boxes:])
            stacks[origin_idx] = s_og[:len(s_og)-n_boxes]
            print(stacks)
            print("======")
            
            continue
        
        if stacks is None:
            stacks = [[] for i in range(len(l)//4)]
        
        box_list = [l[i*4:i*4 + 3].strip(" []") for i in range(len(stacks))]
        
        if box_list[0] == '1':
            next(it_l)
            for s in stacks:
                s.reverse()
            print("======")
            print(stacks)
            print("======")
            move_phase = True
            continue

        for s, it in zip(stacks,box_list):
            if (it != ""):
                s.append(it)
        print(stacks)
print("".join([s.pop() for s in stacks]))
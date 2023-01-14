

def letter_priority(letter):
    return (ord(letter) - 96) % 58

shape_score = [1,2,3]


score = 0
group_list = []
group = []
with open("p1.txt","r") as f:
    for l in f:
        group.append(l.strip())
        if len(group) == 3:
            group_list.append(group)
            group = []


for group in group_list:
    letters = set(group[0])
    letters.intersection_update(set(group[1]))
    letters.intersection_update(set(group[2]))
    print(letters)
    score += letter_priority(letters.pop())
        
print(score)

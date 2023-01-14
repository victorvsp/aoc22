

def letter_priority(letter):
    return (ord(letter) - 96) % 58

shape_score = [1,2,3]


score = 0
with open("p1.txt","r") as f:
    for l in f:
        comp_1 , comp_2 =  l[:len(l)//2] , l[len(l)//2:]
        letters_comp1  = set(c for c in comp_1)
        #print(letters_comp1)
        print([c for c in comp_2 if c in letters_comp1])
        for c in comp_2:
            if c in letters_comp1:
                print(letter_priority(c))
                score += letter_priority(c)
                break
        
print(score)

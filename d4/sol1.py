
# Returns true if A contains B
def contains(A, B):
    return A[0] <= B[0] and B[1] <= A[1]


contains_count = 0
with open("p1.txt","r") as f:
    for l in f:
        asst_pair_str = [p.split('-') for p in l.strip().split(',')]
        (p1, p2) = [[int(p[0]), int(p[1])] for p in asst_pair_str]
        if (contains(p1,p2) or contains(p2,p1)):
            contains_count +=1

print(contains_count)


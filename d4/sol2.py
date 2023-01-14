
# Returns true if A overlaps B
def overlaps(A, B):
    if (A[0] > B[0]):
        A, B = B, A
    return A[1] >= B[0]


contains_count = 0
with open("p1.txt","r") as f:
    for l in f:
        asst_pair_str = [p.split('-') for p in l.strip().split(',')]
        (p1, p2) = [[int(p[0]), int(p[1])] for p in asst_pair_str]
        if (overlaps(p1,p2)):
            contains_count +=1

print(contains_count)



letter_to_number = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "X" : 0,
    "Y" : 1,
    "Z" : 2,
}
shape_score = [1,2,3]
strategy_book = []

with open("p1.txt","r") as f:
    for l in f:
        strategy_book.append(l.split())
print(strategy_book)

total_score = 0
for p in strategy_book:
    op = letter_to_number[p[0]]
    player = letter_to_number[p[1]]

    outcome_score = 0
    if player == (op + 1)%3:  # Player wins
        print("WIN")
        outcome_score = 6
    elif player == op: # Draw
        print("DRAW")
        outcome_score = 3
    else:
        print("LOSS")

    total_score += shape_score[player] + outcome_score 

print(total_score)

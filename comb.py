from itertools import combinations

cards = ['A', 'B', 'C', 'D']
all_combinations = []

for r in range(1, len(cards) + 1):
    combinations_r = combinations(cards, r)
    all_combinations.extend(combinations_r)

for combo in all_combinations:
    print(combo)
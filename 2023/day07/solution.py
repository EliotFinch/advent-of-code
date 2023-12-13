with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

hands = []
for line in lines:
    hand, bid = line.split()
    hands.append(([c for c in hand], int(bid)))

types = [
    'five-of-a-kind',
    'four-of-a-kind',
    'full-house',
    'three-of-a-kind',
    'two-pair',
    'one-pair',
    'high-card'
]

def get_type(hand):
    """Return the type of a hand."""

    unique_elements = list(set(hand))

    # Five of a kind
    if len(unique_elements) == 1:
        return 'five-of-a-kind'
    
    # Four of a kind and full house
    elif len(unique_elements) == 2:

        # Count occurences of one of the elements
        count = 0
        for element in hand:
            if element == hand[0]:
                count += 1
        
        if count in [1, 4]:
            return 'four-of-a-kind'
        else:
            return 'full-house'

    # Three of a kind and two pair
    elif len(unique_elements) == 3:

        # Count occurences of two of the elements
        count1 = 0
        count2 = 0
        for element in hand:
            if element == unique_elements[0]:
                count1 += 1
            elif element == unique_elements[1]:
                count2 += 1
        
        if (count1 in [1,3]) & (count2 in [1,3]):
            return 'three-of-a-kind'
        else:
            return 'two-pair'

    # One pair
    elif len(unique_elements) == 4:
        return 'one-pair'

    # High card
    else:
        return 'high-card'

# Part 1
# ------

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

type_dict = {t: [] for t in types}
for i, (hand, bid) in enumerate(hands):
    type_dict[get_type(hand)].append(i)

total_winnings = 0
rank = 1

for t in types[::-1]:
    
    # The indices of hands of this type
    indices = type_dict[t]

    if len(indices) != 0:
        if len(indices) == 1:
            total_winnings += rank*hands[indices[0]][1]
            rank += 1
        else:
            sorted_hands = [hands[i] for i in indices]
            for i in [4,3,2,1,0]:
                sorted_hands = sorted(
                    sorted_hands, key=lambda c: labels[::-1].index(c[0][i])
                    )
            for hand, bid in sorted_hands:
                total_winnings += rank*bid
                rank += 1

print(total_winnings)

# Part 2
# ------

labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

from collections import defaultdict

type_dict = {t: [] for t in types}
for i, (hand, bid) in enumerate(hands):

    if 'J' in hand:

        # Joker turns into whatever is the most common card (excluding itself)

        counts = defaultdict(int)
        for card in hand:
            if card != 'J':
                counts[card] += 1
        
        # There is a hand which is all jokers...
        if len(counts) != 0:
            joker_target = max(counts, key=counts.get)
        else:
            joker_target = 'A'

        # Replace jokers in the hand
        hand = [joker_target if card == 'J' else card for card in hand]

    type_dict[get_type(hand)].append(i)

total_winnings = 0
rank = 1

for t in types[::-1]:
    
    # Indices of hands of this type
    indices = type_dict[t]

    if len(indices) != 0:
        if len(indices) == 1:
            total_winnings += rank*hands[indices[0]][1]
            rank += 1
        else:
            sorted_hands = [hands[i] for i in indices]
            for i in [4,3,2,1,0]:
                sorted_hands = sorted(
                    sorted_hands, key=lambda c: labels[::-1].index(c[0][i])
                    )
            for hand, bid in sorted_hands:
                total_winnings += rank*bid
                rank += 1

print(total_winnings)
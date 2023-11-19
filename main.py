import random
import argparse


# C: Clubs
# D: Diamonds
# H: Hearts
# S: Spades
suits = ["C", "D", "H", "S"]
# 2: 2
# 3: 3
# ....
# 10: 10
# J: Jack
# Q: Queen
# K: King
# A: Ace
values = {str(i): i for i in range(2, 11)}
for face in ["J", "Q", "K"]:
    values[face] = 10
values["A"] = 11
cards = list(values.keys())

num_values = len(values)
deck_size = len(suits)*num_values


def score_hand(hand):
    # if we get cards that we don't have values for discard them
    return sum([values[c[1:]] for c in hand if c[1:] in values])


def generate_deck():
    # make a new radom deck
    return [f"{suits[i//num_values]}{cards[i%num_values]}" for i in random.sample(range(deck_size), deck_size)]


def is_initial_win_draw(result, win_amount):
    # everybody got 21 with their first 2 cards
    return len([h for _,h in result.items() if score_hand(h) == win_amount]) == len(result)


def is_initial_loss_draw(result, win_amount):
    # everybody got 22 with their first 2 cards
    return len([h for _,h in result.items() if score_hand(h) > win_amount]) == len(result)


def play_cards(result, curr_card, players, dealer, deck, stop_amount = 17):
    # everybody picks cards till their score goes over 17
    for p in players+[dealer]:
        while score_hand(result[p]) < stop_amount and curr_card < len(deck):
            result[p].append(deck[curr_card])
            curr_card = curr_card+1
    return result


def find_winners(result, win_amount):
    # works out winners after the players have drawn their cards
    usable_vals = [score_hand(h) for _,h in result.items() if score_hand(h) <= win_amount]
    max_val = max(usable_vals) if len(usable_vals) > 0 else -1
    return ",".join([p for p,h in result.items() if score_hand(h) == max_val])


def play_blackjack(deck, players, dealer, init_hand = 2, win_amount = 21):
    result = {p: [] for p in players+[dealer]}
    winner = ""
    curr_card = 0
    for _ in range(init_hand):
        for p in players+[dealer]:
            if curr_card >= len(deck):
                break
            result[p].append(deck[curr_card])
            curr_card = curr_card+1

    if is_initial_win_draw(result, win_amount):
        winner = ",".join(players)
    elif is_initial_loss_draw(result, win_amount):
        winner = dealer
    else:
        result = play_cards(result, curr_card, players, dealer, deck)
        winner = find_winners(result, win_amount)
    
    return (winner, result)


if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", help="Input file with preset deck")
    parser.add_argument("--o", help="Output file to save used deck to")
    args = parser.parse_args()

    deck = [] # going to hold the deck in human readable form

    if args.i is not None:
        try:
            with open(args.i, "r") as f:
                deck = [s.strip() for s in f.read().split(",")]
        except:
            print(f"failed to read {args.i}")
            
    if len(deck) == 0: # we didn't get a preset deck
        deck = generate_deck()

    if args.o is not None: # write current deck to output file
        with open(args.o, "w") as f:
            f.write(",".join(deck))

    # we've dealt with setting up the deck - play the actual game
    players = ["sam"]
    dealer = "dealer"
    (winner, hands) = play_blackjack(deck, players, dealer)

    print(winner)
    for p in players+[dealer]:
        print(f"{p}: {','.join(hands[p])}")

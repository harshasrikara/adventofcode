import sys
from functools import cmp_to_key

rank_ordering = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0
}

card_ordering = {
    "A": 12, "K": 11, "Q": 10, "J": -1, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0
}

def get_rank(hand: str) -> str:
    freq = {}
    for ch in hand:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    if len(freq) == 1:
        return "Five of a kind"
    elif len(freq) == 2:
        for key in freq:
            if freq[key] == 4 or freq[key] == 1:
                if "J" in hand:
                    return "Five of a kind"
                return "Four of a kind"
            else:
                if "J" in hand:
                    return "Five of a kind"
                return "Full house"
    elif len(freq) == 3:
        for key in freq:
            if freq[key] == 3:
                if "J" in hand:
                    return "Four of a kind"
                return "Three of a kind"
            elif freq[key] == 2:
                if "J" in hand:
                    if freq["J"] == 2:
                        return "Four of a kind"
                    if freq["J"] == 1:
                        return "Full house"
                return "Two pair"
    elif len(freq) == 4:
        if "J" in hand:
            return "Three of a kind"
        return "One pair"
    elif len(freq) == 5:
        if "J" in hand:
            return "One pair"
        return "High card"
    else:
        "PROBLEM"

    return ""

def get_joker_rank(hand: str) -> str:
    rank = get_rank(hand)

    if "J" not in hand:
        return rank


    if rank == "Five of a kind":
        return "Five of a kind"
    
    if rank == "Four of a kind":
        return "Five of a kind"
    
    if rank == "Three of a kind":
        return "Four of a kind"
    
    if rank == "High card":
        return "One pair"
    
    if rank == "One pair":
        return "Two pair"
    
    if rank == "Two pair":
        return "Three of a kind"


def parse(file):
    hand_to_bid = {}
    for line in file.readlines():
        line = line.strip('\n')
        print(line)

        terms = line.split(" ")
        hand, bid = terms[0], terms[1]
        hand_to_bid[hand] = bid
    
    return hand_to_bid

def get_hand_list(hand_to_bid: dict[str, int]) -> list[str]:
    hands = []
    for key in hand_to_bid:
        hands.append(key)
    
    return hands

def get_hand_to_rank_map(hands: list[str]) -> dict[str, str]:
    hand_to_rank = {}
    for hand in hands:
        hand_to_rank[hand] = get_rank(hand)

    return hand_to_rank

def cmp_hands(hand1: str, hand2: str):
    hand1_rank = get_rank(hand1)
    hand2_rank = get_rank(hand2)

    if rank_ordering[hand1_rank] > rank_ordering[hand2_rank]:
        return 1
    elif rank_ordering[hand1_rank] < rank_ordering[hand2_rank]:
        return -1
    else:
        for i in range(len(hand1)):
            if card_ordering[hand1[i]] > card_ordering[hand2[i]]:
                return 1
            elif card_ordering[hand1[i]] < card_ordering[hand2[i]]:
                return -1
        return 0

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day7/input.txt")

    hand_bid = parse(f)
    print(hand_bid)

    hands = get_hand_list(hand_bid)

    new = sorted(hands, key=cmp_to_key(cmp_hands))

    print(new)

    sum = 0
    for i in range(len(new)):
        sum = sum + int(hand_bid[new[i]]) * (i+1)

    print(sum)
    return 0


if __name__ == '__main__':
    sys.exit(main())
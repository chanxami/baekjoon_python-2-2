import math

def min_exchanges(G1, S1, B1, G2, S2, B2):
    moves = 0

    if B1 < B2:
        needed_bronze = B2 - B1
        need_silver_for_bronze = (needed_bronze + 8) // 9
        spare_silver = S1 - S2 if S1 > S2 else 0
        if spare_silver >= need_silver_for_bronze:
            S1 -= need_silver_for_bronze
            B1 += need_silver_for_bronze * 9
            moves += need_silver_for_bronze
        else:
            if spare_silver > 0:
                moves += spare_silver
                S1 -= spare_silver
                B1 += spare_silver * 9
                need_silver_for_bronze -= spare_silver
            extra_gold = G1 - G2
            gold_needed = (need_silver_for_bronze + 8) // 9
            if gold_needed > extra_gold:
                return -1
            G1 -= gold_needed
            moves += gold_needed
            S1 += gold_needed * 9
            S1 -= need_silver_for_bronze
            B1 += need_silver_for_bronze * 9
            moves += need_silver_for_bronze

    if S1 < S2:
        needed_silver = S2 - S1
        extra_gold = G1 - G2
        if extra_gold > 0:
            gold_needed = (needed_silver + 8) // 9
            if gold_needed <= extra_gold:
                G1 -= gold_needed
                moves += gold_needed
                S1 += gold_needed * 9
            else:
                G1 -= extra_gold
                moves += extra_gold
                S1 += extra_gold * 9
        if S1 < S2:
            needed_silver = S2 - S1
            extra_bronze = B1 - B2 if B1 > B2 else 0
            possible = extra_bronze // 11
            if possible < needed_silver:
                return -1
            B1 -= needed_silver * 11
            S1 += needed_silver
            moves += needed_silver

    if G1 < G2:
        needed_gold = G2 - G1
        required_extra_silver = needed_gold * 11
        current_extra_silver = S1 - S2 if S1 >= S2 else 0
        if current_extra_silver < required_extra_silver:
            additional_silver_needed = required_extra_silver - current_extra_silver
            extra_bronze = B1 - B2 if B1 >= B2 else 0
            if extra_bronze < additional_silver_needed * 11:
                return -1
            B1 -= additional_silver_needed * 11
            S1 += additional_silver_needed
            moves += additional_silver_needed
        if S1 - S2 < needed_gold * 11:
            return -1
        S1 -= needed_gold * 11
        G1 += needed_gold
        moves += needed_gold

    if G1 >= G2 and S1 >= S2 and B1 >= B2:
        return moves
    else:
        return -1

if __name__ == "__main__":
    G1, S1, B1 = map(int, input().split())
    G2, S2, B2 = map(int, input().split())
    result = min_exchanges(G1, S1, B1, G2, S2, B2)
    print(result)

from random import randrange


def roll_dice(dices):
    dice = []
    for i in range(dices):
        dice.append(randrange(1, 7))
    dice.sort()
    return dice


def players_turn():
    pl = 0  # player 1 or 2
    keeptotal = []  # all dices for players at each round
    for i in range(2):  # rounds
        flag = True  # for the case of not keeping the dice there is a choice of keeping some of the dices and the
        # other that they didn't pick re-rolled
        cnt = 0  # counter of player's chances to throw 3 times the dice
        keep = []  # the dices that player keeps
        sm = []  # the sum of all dices at this round
        d = [""]  # dices rolled
        keeptotal.append(f"Player {pl + 1}'s round's rolled dices:")
        while cnt < 3:  # 3 dice throws is allowed
            if not flag:  # in case of player chooses the dices these part of code must not run. Next player plays
                break
            cnt += 1  # counter of dice throws in a round
            while len(d) != 0:  # in case of d's length being 0 - except from the beginning - program should go to the
                # next player
                print(f"Player {pl % 2 + 1}:", end=" ")
                r = input("Press r to roll dice: ")
                print("")
                if r == "R" or r == "r":
                    break
            d = roll_dice(5 - len(keep))  # the rest of the player's dices didn't keep is allowed to throw
            temp = d.copy()
            keeptotal.append(temp)
            pos = ""
            while pos != 0 and len(d) > 0:  # in case of all dices have chosen the next player plays rapidly
                print(f"Dices thrown: {d}")
                for j in range(len(d)):
                    sm.append(d[j])
                for j in range(len(keep)):
                    sm.append(keep[j])
                print(f"Total dices: {sm}\n")
                y = players_picks(pl % 2, sm)
                if y == 1:  # in case of this value is 1 don't run the code below
                    flag = False
                    break
                sm.clear()
                while flag and cnt < 3:  # at the 3rd try on rolling dice player must choose the numbers, otherwise
                    # player loses the round. So the below code must run 2 times maximum
                    while True:
                        pos = input("Which dices do you want to keep? Press the position of dice or press 0 if you "
                                    "want to keep them: ")
                        pos = pos.strip()
                        if "0" <= pos <= "5" and pos.isdigit():
                            break
                        else:
                            print("Insert a valid position", end=". ")
                    print("")
                    pos = int(pos)
                    if pos == 0:  # in case of user choosing zero program allows player to roll the dice if there is
                        # his first or second try at the round otherwise the next player plays
                        break
                    if pos <= len(d):
                        keep.append(d.pop(pos - 1))
                        if len(d) == 0:
                            break
                    else:
                        print("Insert a valid position", end=". ")
                        print("")
                        continue
                    print(f"Dices thrown: {d}")
                    print(f"Kept: {keep}")
                    print("")
                if cnt == 3 or len(d) == 0:
                    print("You didn't append something.")
                    print("")
                    break
        pl += 1  # changes the player
    return keeptotal


def players_picks(p, dice):
    global score
    scoretemp = [{"ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0},
                 {"ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0}]  # temporary scoretable for
    # each round
    flag = True  # validity check
    for i in range(len(dice)):
        if dice[i] == 1:
            scoretemp[p]["ones"] += 1
        elif dice[i] == 2:
            scoretemp[p]["twos"] += 2
        elif dice[i] == 3:
            scoretemp[p]["threes"] += 3
        elif dice[i] == 4:
            scoretemp[p]["fours"] += 4
        elif dice[i] == 5:
            scoretemp[p]["fives"] += 5
        else:
            scoretemp[p]["sixes"] += 6
    for ks, vl in scoretemp[p].items():
        if score[p][ks] == -1:
            print(f"{ks}: {vl}")
    print("")
    while flag:
        ch2 = input("Chooce the number you want to hold from 'ones' to 'sixes' or press 0 to continue: ")
        print("")
        ch2 = ch2.strip()
        ch2 = ch2.lower()
        if (ch2 == "ones" or ch2 == "twos" or ch2 == "threes" or ch2 == "fours" or ch2 == "fives" or ch2 == "sixes"
                or ch2 == "0"):
            for ks, vl in score[p].items():
                if (ks == ch2 and vl == -1) or ch2 == "0":  # the input value is valid only when the score value is
                    # not touched (value: -1)
                    flag = False
                    break
            else:
                print("Insert a valid number", end=". ")
        else:
            print("Insert a valid number", end=". ")
    if ch2 != "0":
        if scoretemp[p][ch2] == 0:  # in case of player chooses value that has the sum of zero appends at the
            # scoretable the value of -2
            score[p][ch2] = -2
    if ch2 == "ones":
        for i in range(len(dice)):
            if dice[i] == 1:
                score[p][ch2] += 1
    elif ch2 == "twos":
        for i in range(len(dice)):
            if dice[i] == 2:
                score[p][ch2] += 2
    elif ch2 == "threes":
        for i in range(len(dice)):
            if dice[i] == 3:
                score[p][ch2] += 3
    elif ch2 == "fours":
        for i in range(len(dice)):
            if dice[i] == 4:
                score[p][ch2] += 4
    elif ch2 == "fives":
        for i in range(len(dice)):
            if dice[i] == 5:
                score[p][ch2] += 5
    elif ch2 == "sixes":
        for i in range(len(dice)):
            if dice[i] == 6:
                score[p][ch2] += 6
    if ch2 != "0":
        for ks, vl in score[p].items():
            if score[p][ks] == -2:
                print(f"{ks}:{vl + 2}")
            else:
                print(f"{ks}:{vl + 1}")  # it's because the initial score value is -1
        print("")
        return 1  # program returns 1 to prevent running some lines of the program
    else:
        return 0


def main():
    s1 = 0  # total score of Player 1
    s2 = 0  # total score of Player 2
    for i in range(6):  # 6 Rounds
        print(f"Round {i + 1}: \n")
        k = players_turn()
        print(k)
        print("")
    for ks, vl in score[0].items():
        if score[0][ks] == -2:
            s1 = s1 + vl + 2
        else:
            s1 = s1 + vl + 1
    for ks, vl in score[1].items():
        if score[1][ks] == -2:
            s2 = s2 + vl + 2
        else:
            s2 = s2 + vl + 1
    if s1 > s2:
        print(f"Player 1 wins! {s1}-{s2}")
    elif s1 < s2:
        print(f"Player 2 wins! {s1}-{s2}")
    else:
        print(f"Draw. {s1}-{s2}")


score = [{"ones": -1, "twos": -1, "threes": -1, "fours": -1, "fives": -1, "sixes": -1},
         {"ones": -1, "twos": -1, "threes": -1, "fours": -1, "fives": -1, "sixes": -1}]

main()

# 73:20h

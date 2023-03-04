from random import *

def nim(n):
    return 1  # 1 is always a legal move


def nim2(n):
    return randint(1, min(n, 3))    # n is guaranteed to be at least one and


# print('Computer pick', nim2(4))


def nim_human(n):
    human_pick = int(input('Enter the number of sticks you want to pick; 1, 2, 3 :'))
    possible_input = list(range(1, min(n, 3)+1))
    print(possible_input)
    if possible_input.__contains__(human_pick):
        pick = human_pick
        return pick
    else:
        print('Illegal move')
        nim_human(n)


# print('I pick', nim_human(4))


def nim_best(n):
    taken = n % 4
    if taken:
        return taken
    else:
        # Taken is 0, we loose. Just take randomly
        return randint(1, min(n, 3))


player_pool = [nim, nim2, nim_best, nim_human]


def pick_players():
    players = []

    while len(players) < 2:
        print("These are the players %s" % "/".join(player_pool.keys()))
        p = input("Name one: ")
        if p not in player_pool.keys():
            print("Not a valid player. Select again: ")
            continue
        players.append(p)
    print("Player %s begins, player %s plays second." % tuple(players))
    return players


# transform to Dictionary
player_pool = {p.__name__: p for p in player_pool}


def game():
    while True:
        n = int(input('Enter the number of sticks: '))
        if n > 0: break

    current, other = tuple(pick_players())

    while n > 0:
        print("Heap has %d sticks." % n)
        taken = player_pool[current](n)
        print("%s takes %d sticks.\n" % (current, taken))

        n -= taken

        current, other = other, current

    print("{} won the game", format(other.__name__))
# def game_controller():


game()

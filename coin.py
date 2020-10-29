import random
toss = ('Heads', 'Tails')
heads = 0
tails = 0
games = 0

print ('Hit Q to quit')
while True:
    flip = random.choice(toss)
    choice = input('Type Heads or Tails: ')
    if choice == 'q' or choice == 'Q':
        print("Game ended! :/")
        print("Coin Toss stats:")
        print("Games played = {}".format(games))
        print("heads = {}".format(heads))
        print("tails = {}".format(tails))
        break

    if choice == flip:
        print("{}.You Win!".format(flip))
        games += 1 #incrementing games

    else:
        print("{}.You lost :(".format(flip))
        games += 1

    if flip == "heads":
        heads += 1
    elif flip == "tails":
        tails += 1
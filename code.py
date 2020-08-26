# 1. creating a deck with lambda, map and zip

vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']

suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck = tuple(map(lambda v: list(zip([v]*4, suits)), vals))

# 2. write a function without lambda, map and zip to create a deck

def create_deck():
    """Function returns a deck of cards
    Returns:
        tuple of tuples: a single deck of cards as an immutable object
    """
    vals = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = []
    for val in vals:
        for suit in suits:
            tup = (val, suit)
            deck.append(tup)
    return tuple(deck)

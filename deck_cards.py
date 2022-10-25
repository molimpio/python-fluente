"""
Example chapter 1 book Python Fluente
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FreechDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FreechDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(f'Created beer card, rank: {beer_card.rank}, suit: {beer_card.suit}')

    deck = FreechDeck()
    print(f'Quantity decks: {len(deck)}')
    print(f'First deck: {deck[0]}')
    print(f'Last deck: {deck[-1]}')

    from random import choice
    print(f'Random deck: {choice(deck)}')

    for card in deck:
        print(f'Card: {card}')

    print(f'Use contains {Card("Q", "hearts") in deck}')

    for card in sorted(deck, key=spades_high):
        print(f'Use sorted {card}')

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank >= 10:
            self.points = 10
        elif rank == 1:
            self.points = 11
        else:
            self.points = rank
    def __repr__(self):
        d = {11: 'Jack', 12:'Queen', 13:'King', 1:'Ace'}

        if self.rank > 10 or self.rank == 1:
            return f'{d[self.rank]} of {self.suit}'
        return f'{self.rank} of {self.suit}'

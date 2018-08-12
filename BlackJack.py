

    """Kreuz, Herz, Pick, Karo"""
farben = ['KR', 'HE', 'PI', 'KA']

raenge = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

werte = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

class Karte(self, farbe, rang):
    """docstring for Karte"""
    def __init__(self, farbe, rang):
        super(Karte, self).__init__()
        self.farbe = farbe
        self.rang = rang

            
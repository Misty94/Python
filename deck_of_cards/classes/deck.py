from . import card

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            point = i
            for i in range(1,14):
                if i > 10:
                    point = 10
                else: 
                    point = i
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                
                self.cards.append( card.Card( s , point , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def show_hand(self):
        pass


import random

# Card
#● A card has two properties: a rank and a suit.
#● A card’s rank is an ordered value. There are 13 ranks. From lowest to highest, a rank can be one of the values: { 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A }
#● A card’s suit is an unordered value. A suit can be one of { ♣, ♦, ♥, ♠ }. These are spoken as “clubs”, “diamonds”, “hearts”, and “spades”.
#● A card is defined as a rank and a suit. We display them as rank + suit, for example, 2♥, 10♦, Q♦, etc.

class Cards:
    def __init__(self):
        self.cards = []
        self.cards_original = [] #original list for shorting the cards
        suits = ["\u2663", "\u2665", "\u2666", "\u2660"] #2663:club, 2665:heart,2666:diamond, 2660:spade  
        ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        rank_dict = {11:"J", 12:"Q", 13:"K", 14:"A"}

#        for suit in suits:
#            for rank in ranks:
#                if rank in rank_dict:
#                    card_name = [rank_dict[rank], suit]
#                else:
#                    card_name = [rank, suit]
#                self.cards.append(card_name)

        for suit in suits:
            for rank in ranks:
                if rank in rank_dict:
                    card_name = f"{rank_dict[rank]} of {suit}" # for fancy output like : A of ♠
                else:
                    card_name = f"{rank} of {suit}" # for fancy output like : A of ♠
                self.cards.append(card_name)
                self.cards_original.append(card_name)

# Deck
#● A deck of cards is an ordered collection of cards. It will start with 52 cards, one card for every combination of rank and suit.
#● Players can draw() from a deck. This means that they take the top card from the deck and add it to their hand.
#● You can shuffle() a deck, which randomizes the order of the cards in the deck.

class Deck:
    def __init__(self, players):
        self.cards = Cards().cards
        self.players = players
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) > 0:
            card = self.cards.pop() #pop to take the top card from the deck
            #we append cards in the Game class now as we want multiplayer
            return card
        else:
            print ("No cards left in the Deck")
            return None #we return None to get rid of the "not supported between instances of 'NoneType' and 'NoneType'" errors

# Player
#● Players have a hand of cards, represented as an ordered collection of cards.
#● Players can draw() from a deck. (See definition above).

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name


class Game:
    def __init__(self):
        
        self.player_number = int(input("Please enter the number of players:"))
        self.players = [Player(f"Player {n+1}") for n in range(self.player_number)] # we calculate the players number.
        self.deck = Deck(self.players) 
        self.list1 = Cards().cards_original #list 1 for the original deck order


    def sort_key(self, card): #use the index of the cards in the original card list
        return self.list1.index(card)
            
    def play(self):
        while True:
            for player in self.players: #for loop for each player
                option = input(f"{player.name} Press 'd' to draw a card, 's' to shuffle the cards or 'q' to quit.")
                if option == 'd':
                    card = self.deck.draw() 
                    if card:
                        player.hand.append(card) #moved the card append here so each player gets its own cards
                        print(f"{player.name} draw {card}")
                        self.list2 = player.hand #list of the players hand
                        self.sorted_hand = sorted(self.list2, key=self.sort_key) #sorted hand by the original deck
                        print(f"{player.name} Your hand is {self.sorted_hand}")

                    else: 
                        print("No cards left.")
                elif option == 's':
                    self.deck.shuffle()
                    print("Deck shuffled.")
                elif option == 'q':
                    print("Exiting game!")
                    return
                else:
                    print("Press 'd' to draw a card, 's' to shuffle the cards or 'q' to quit.")  


if __name__ == "__main__":
    g = Game()
    g.play()
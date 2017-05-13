# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        out = ""
        for i in self.cards:
            out = out + ' ' + str(i)
        return 'The hand contains ' + out    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        if len(self.cards) == 0:
            return 0
        else:
            val = 0
            contain_ace = False
            for i in range(len(self.cards)):  
                if self.cards[i].get_rank() == 'A' and not contain_ace:
                    contain_ace = True
                    val = VALUES[str(self.cards[i].get_rank())] + val + 10
                elif self.cards[i].get_rank() == 'A' and contain_ace:
                    val = VALUES[str(self.cards[i].get_rank())] + val
                else:
                    val = VALUES[str(self.cards[i].get_rank())] + val
            if contain_ace and val > 21:
                return val - 10
            else:
                return val
    def draw(self, canvas, pos, player):
        # draw a hand on the canvas, use the draw method for cards
        if player:
            for i in range(len(self.cards)):
                self.cards[i].draw(canvas,[pos[0]+72*i,pos[1]])
        elif not player and in_play:
            canvas.draw_image(card_back, [pos[0],pos[1]], CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            self.cards[1].draw(canvas,[pos[0]+72,pos[1]])
        else:
            for i in range(len(self.cards)):
                self.cards[i].draw(canvas,[pos[0]+72*i,pos[1]])
            

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for s in SUITS:
            for rank in RANKS:
                self.cards.append(Card(s, rank))    
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        delt = self.cards[random.randrange(0, len(self.cards))]
        self.cards.remove(delt)
        return delt
    def __str__(self):
        # return a string representing the deck
        out = ""
        for i in self.cards:
            out = out + ' ' + str(i)
        return 'The Deck contains ' + out



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, deck
    global dealer_hand

    # your code goes here
    in_play = True
    deck = Deck()
    deck.shuffle() 
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    


def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    global outcome, in_play, score
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() > 21:
                outcome = 'You have busted' 
                score = score - 1
                in_play = False
        else:
            outcome = 'You have busted'
            score = score - 1
            in_play = False
    else:
        return outcome
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if player_hand.get_value() > 21:
        outcome = 'You have busted'
        score = score - 1
    else:
        if dealer_hand.get_value() < 17:
            while (dealer_hand.get_value() < 17):
                dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer busted'
            score = score + 1
        else:
            out = dealer_hand.get_value() >= player_hand.get_value()
            if out:
                outcome = 'Dealer wins'
                score = score - 1
            else:
                outcome = 'Player wins'
                score = score + 1
    # assign a message to outcome, update in_play and score
    in_play = False
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    player_hand.draw(canvas,[120,300], True)
    dealer_hand.draw(canvas,[120,150], False)
    if not in_play:
        canvas.draw_text(outcome, [450,100], 16, 'White')
    canvas.draw_text('The score is: ' + str(score),[450,50],16,'White')    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)



# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
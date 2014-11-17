# Mini-project #6 - Blackjack
# Zhizheng Wang

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
deck = []

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
        self.card = []

    def __str__(self):
        s = ""
        for c in self.card:
            s = s + str(c) + ' '
        s = "Hand contains " +  s
        return s

    def add_card(self, card):
        self.card.append(card)
        return self.card

    def get_value(self):
        sum = 0
        for card in self.card:
            rank = card.get_rank()
            sum +=   VALUES[rank]
        for card in self.card:
            rank = card.get_rank()    
            if rank == 'A' and sum <= 11:
                sum += 10
        return sum

   
    def draw(self, canvas, pos):
        p = pos
        for card in self.card:
            card.draw(canvas, p)
            p[0] = p[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER,
                              CARD_BACK_SIZE, [85,197], CARD_BACK_SIZE)

# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append((Card(i,j)))

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        deal = self.deck[len(self.deck)-1]
        self.deck.pop(len(self.deck)-1)
        return deal
    
    def __str__(self):
        def string_list_join(string_list):
            ans = ""
            for i in range(len(string_list)):
                ans += str(string_list[i]) + " "
            return ans
        s = "Deck contains " + string_list_join(self.deck)
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, score, msg
    msg = ""
    #print ""
    if in_play == True:
        score -= 1
        msg = "You deal during the round and you lose!"
        in_play = False
    else:
        deck = Deck()
        deck.shuffle()
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        #print "Dealer's " + str(dealer_hand),", while Player's " + str(player_hand)+ "."
        in_play = True
        outcome = "Hit or stand?"

def hit():
    global outcome, in_play, player_hand, dealer_hand, deck, score, msg
    if in_play == True:
        player_hand.add_card(deck.deal_card())
        outcome = "Hit or stand?"
        #print "Player's " + str(player_hand)
        if player_hand.get_value() > 21:
            msg = "You have busted and lost!"
            score -= 1
            in_play = False
            outcome = "New deal?"

def stand():
    global outcome, in_play, player_hand, dealer_hand, deck, score, msg
    if in_play ==True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            #print "Dealer's " + str(dealer_hand)
        if dealer_hand.get_value() > 21:
            score += 1
            msg =  "Dealer have busted and you win!"
        else:
            if dealer_hand.get_value()>= player_hand.get_value():
                score -= 1
                msg =  "Dealer Wins!"
            else:
                score += 1
                msg = "You Win!"
        in_play = False
        outcome = "New deal?"
        
# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [200,75], 50, "Blue")
    canvas.draw_text("Score : " + str(score), [80,520], 24, "Red")
    canvas.draw_text("Dealer :", [80,130], 30, "Black")
    canvas.draw_text("Player :", [80,285], 30, "Black")
    canvas.draw_text(outcome, [200,285], 30, "Yellow")
    canvas.draw_text(msg, [80,480], 30, "Yellow")
    dealer_hand.draw(canvas, [50,150])
    player_hand.draw(canvas, [50,300])

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

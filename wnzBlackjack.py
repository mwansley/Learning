# Wanz Blackjack Game
import random

# Create Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']}  of {self.suit}"

# Create Deck Class
class Deck:
    # constructor
    def __init__(self):
      # create list and rank of cards
      self.cards = []
      suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
      ranks = [
              {"rank": "A", "value": 10},
              {"rank": "K", "value": 10},
              {"rank": "Q", "value": 10},
              {"rank": "J", "value": 10},
              {"rank": "10","value": 10},
              {"rank": "9", "value": 9},
              {"rank": "8", "value": 8},
              {"rank": "7", "value": 7},
              {"rank": "6", "value": 6},
              {"rank": "5", "value": 5},
              {"rank": "4", "value": 4},
              {"rank": "3", "value": 3},
              {"rank": "2", "value": 2},
              {"rank": "1", "value": 1}
          ]    
      for suit in suits:
        for rank in ranks:
            self.cards.append(Card(suit, rank))


    # Shuffle the deck
    def shuffle(self):
        if len(self.cards) > 1:
          random.shuffle(self.cards)
      
    # Deal number of cards 
    def deal(self, number):
      cards_dealt = []
      for x in range(number):
        if len(self.cards) > 0:
          card = self.cards.pop()
          cards_dealt.append(card)
      return cards_dealt 

# Create Hand Class
class Hand:
  # player & dealer obj
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer 

  def add_card(self, card_list):
      self.cards.extend(card_list)
  
  # add each card value
  def calculate_value(self):
      self.value = 0
      has_ace = False
    
      for card in self.cards:
          card_value = int(card.rank["value"])
          self.value += card_value 
          if card.rank["rank"] == "A":
            has_ace = True

      if has_ace and self.value > 21:
            self.value -= 10 # sets ace value to 1 rather than 10

  # calculate card value
  def get_value(self):
      self.calculate_value()
      return self.value

  def is_blackjack(self):
      return self.get_value() == 21

  # use of ternary operator
  # used 3 single quotes to allow str w/apostrophe
  def display(self, show_all_dealer_cards=False):
      print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
      for index, card in enumerate(self.cards):
          if index == 0 and self.dealer \
          and not show_all_dealer_cards and not self.is_blackjack():
              print("hidden")
          else:
              print(card)

      if not self.dealer:
          print("Value:", self.get_value())
          print() # blank line
      

# Create Game Class
class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
          try:        
            games_to_play = int(input('How many games would you like to play? '))
          except:
              print("You must enter a number...")

        # main game loop 
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            # separate by * divider
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            # check for a winner, start new game
            if self.check_winner(player_hand, dealer_hand):
                   continue 
              
            # check if player chooses to hit or stand
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("\nPlease choose 'Hit' or 'Stand' ").lower()
                print()
                # Loop until valid input
                while choice not in ["h", "s", "Hit", "Stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                  
            if self.check_winner(player_hand, dealer_hand):
                continue
    
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
    
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
        
            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print()
            print("Final Results")
            print("Your hand: ", player_hand_value)
            print("Dealer's hand: ", dealer_hand_value)
        
            self.check_winner(player_hand, dealer_hand, True)
                
        print("\nThanks for playing!!")
              
    # check if there's a winner
    def check_winner(self, player_hand, dealer_hand, game_over=False):
      if not game_over:
        if player_hand.get_value() > 21:
            print('You busted. Dealer wins! ')
            return True
        elif dealer_hand.get_value() > 21:
            print('Dealer busted!!. YOU WIN!!!')
            return True 
        elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
            print("It's a tie, YOU BOTH WIN!!!!")
            return True
        elif player_hand.is_blackjack():
            print('You have blackjack. YOU WIN!!!')
            return True    
        elif dealer_hand.is_blackjack():
            print('Dealer has blackjack. Dealer wins!')
            return True
      else:
          if player_hand.get_value() > dealer_hand.get_value():
              print("YOU WIN!!")
          elif player_hand.get_value() == dealer_hand.get_value():
              print("It's a tie!")
          else:
              print("Dealer wins.")
          return True
      return False
           
g = Game()
g.play()

  # shuffle()
  # card = deal(1)[0]
  # cards_dealt = deal(2)
  # card = cards_dealt[0]
  # rank = card[1]
  
  # if rank == "A":
  #   value = 11
  # elif rank == "J" or rank == "K" or rank == "Q":
  #   value = 10
  # else:
  #   value = rank 
  




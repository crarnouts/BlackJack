# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:50:31 2021

@author: Corey_Arnouts
"""

import numpy as np
import random



def BlackJackStrategy(hand, dealer_card):
    hard_count=sum(hand)
    cards=len(hand)
    aces_count= 1*(1 in hand)
    soft_count=hard_count
    good_cards=[1,7,8,9,10]
    
    if cards<2:
        return 'Not enough cards'
    
    if hard_count<=11:
        soft_count= hard_count + 10*aces_count
        
    if cards==2 and soft_count==21:
        return 'Blackjack'
    
    
    if soft_count>=19:
        return 'Stay'
    
    if hand==[9,9] and dealer_card not in [1,7,10]:
        return 'Split'
    
    if hard_count>=17 :
        return 'Stay'

    
    if cards>2:
        if hard_count==soft_count:
            if hard_count<=11:
                return 'Hit'

            if hard_count==12 and dealer_card <=3:
                return 'Hit'

            if dealer_card in good_cards:
                return 'Hit'

            return 'Stay'
        
        
        if soft_count<=17:
            return 'Hit'
        
        if soft_count==18 and dealer_card in [1,9,10]:
            return 'Hit'
        
        
        
        return 'Stay'
    
            
        
    
    if cards==2:
        
        if hand[0]==hand[1]:
            card= hand[0]
            
            if card==1:
                return 'Split'
            
            if card==8 and dealer_card!=1:
                return 'Split'
            
            if card in [2,3,7] and dealer_card not in [1,8,9,10]:
                return 'Split'
            
            if card==6 and dealer_card not in good_cards:
                return 'Split'
            
            if card==4 and dealer_card in [5,6]:
                return 'Split'
            
        if hard_count==soft_count:
            
            if hard_count==11 and dealer_card!=1:
                return 'Double'
            
            if hard_count==10 and dealer_card not in [1,10]:
                return 'Double'
            
            if hard_count==9 and dealer_card not in ([2]+ good_cards):
                return 'Double'
            
            if hard_count<=11:
                return 'Hit'

            if hard_count==12 and dealer_card <=3:
                return 'Hit'

            if dealer_card in good_cards:
                return 'Hit'

            return 'Stay'
            
        
        if hard_count!=soft_count:
            

                
            if soft_count==18:
                
                if dealer_card not in ([2]+good_cards):
                    return 'Double'
                
                if dealer_card in [2,7,8]:
                    return 'Stay'
                
            if soft_count==17 and dealer_card in [3,4,5,6]:
                return 'Double'
            
            if soft_count in [15,16] and dealer_card in [4,5,6]:
                return 'Double'
            
            if soft_count in [13,14] and dealer_card in [5,6]:
                return 'Double'
            
            return 'Hit'
        
        
"""        
deck=np.array([1,2,3,4,5,6,7,8,9,10,10,10,10])
player_hand =[]
player_hand.append(deck[0])

        


deck=np.array([10,11,1,2,3,4,5,6,7,8,9,10,10,10,10])
player_hand='q'
if type(player_hand)==str:
    print("string")
else:
    print("not string")
    #player_hand = []
    #player_hand.append(deck[0])
    #player_hand.append(deck[1])
    #deck = np.delete(deck,[0,1])
    
    
deck
player_hand


var2 = 'this is variable #2'
if type(var2) is str:
    print('your variable is a string')
else:
    print('your variable IS NOT a string')
    
    
var = 1
if type(var) == int:
   print('your variable is an integer')



sample_text = "Hello"
# Check if the type of a variable is string
if isinstance(sample_text, str):
    print('Type of variable is string')
else:
    print('Type is variable is not string')

"""



############## SIMULATE ONE HAND OF BLACKJACK #############################
def blackjack_hand_result(bet=10, player_hand='q', dealer_card='q', hard_code= 4,deck=np.array([10,11,1,2,3,4,5,6,7,8,9,10,10,10,10])):
    #Deck of cards, 4 types of 10
    
    #deck = np.random.shuffle(deck)
    
    #hard stay condition for split aces
    
    hard_stay=False
    
    #Creating a random hand if none is input
    
    if type(player_hand)==str:
        player_hand = []
        player_hand.append(deck[0])
        player_hand.append(deck[1])
        deck = np.delete(deck,[0,1])
        
    #Turning on hard stay for split aces
        
    if player_hand==[1]:
        hard_stay==True
        
    #Adding a 2nd card to hand after splits    
        
    while len(player_hand)<2:
        player_hand.append(deck[0])
        deck = np.delete(deck,0)
        
    #Creating dealer card, and dealer cards
        
    if type(dealer_card)==str:
    
        dealer_card=deck[0]
        deck = np.delete(deck,0)
        
    dealer_cards=[dealer_card]
    
    
    #If hard stay condition is false
        
    if hard_stay==False:
        
        #Seeing if player hit blackjack
        
        
        if BlackJackStrategy(player_hand, dealer_card) == 'Blackjack':
            
            #Seeing if casino also hit blackjack, in which case tie
            
            dealer_cards.append(deck[0])
            deck = np.delete(deck,0)
            if 1 in (dealer_cards):
                if sum(dealer_cards)==11:
                    return 0, deck
                
             #Blackjack bonus, if not   

            return bet*1.5, deck
        
        if type(hard_code)== str:
            if hard_code=='Hit':
                player_hand.append(deck[0])
                deck = np.delete(deck,0)
                return blackjack_hand_result(bet, player_hand, dealer_card, hard_code= 4)
            
            if hard_code=='Double':
                if len(player_hand)==2:
                    player_hand.append(deck[0])
                    deck = np.delete(deck,0)
                    bet= bet*2
                    if sum(player_hand)>21:
                        return 0 - bet, deck
                    
                else:
                    return 'Double Not Possible', deck
                
            if hard_code=='Split':
                
                
                if len(player_hand)==2: 
                    
                    if player_hand[0]==player_hand[1]:
                        
                        
                        res, deck = blackjack_hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split', deck = deck)
                        res2, deck = blackjack_hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split', deck = deck)
                        res = res + res2

                        return res, deck
                        
                
                    
                    else:
                        return blackjack_hand_result(bet=bet, player_hand= player_hand, dealer_card=dealer_card)

                    
                else:
                    return blackjack_hand_result(bet=bet, player_hand=player_hand, dealer_card=dealer_card)

                    
        
        
        else:
        #Seeing how often it says to 'hit'

            while BlackJackStrategy(player_hand, dealer_card) == 'Hit':
                #Adding one card for every hit
                player_hand.append(deck[0])
                deck = np.delete(deck,0)

                #Player loses bet if hand goes above 21
                if sum(player_hand)>21:
                    return (0- bet), deck

                #If player Doubles

            if BlackJackStrategy(player_hand, dealer_card)=='Double':
                #He gets exactly one extra card and the bet size is doubled
                player_hand.append(deck[0])
                deck = np.delete(deck,0)
                bet= bet * 2
                if sum(player_hand)>21:
                    return (0- bet), deck

                #If player Splits

            if BlackJackStrategy(player_hand, dealer_card)== 'Split':

                #Runs the sim twice, as different hands, slightly less variance than real life, but it's okay

                res, deck = blackjack_hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split', deck = deck)
                res2, deck = blackjack_hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split', deck = deck)
                res = res + res2
                

                return res, deck
        
        while True:
            #Plays out the blackjack hand from dealer's side
            
            #Give dealer extra card if loop hasn't broken
            dealer_cards.append(deck[0])
            deck = np.delete(deck,0)
            
            
            #Keep track of sum of dealer's cards
            dealer_score= sum(dealer_cards)
            
            #Keep track of soft score if dealer has an ace
            
            soft_score= dealer_score
            if dealer_score<=11 and 1 in dealer_cards:
                soft_score+=10
                
            #If dealer gets blackjack you lose even if you have 21
            if len(dealer_cards)==2 and soft_score==21:
                return (0-bet), deck
                
            #Keeps track of player's score     
            player_score=sum(player_hand)
            
            #Uses soft score if that is better for player
            if player_score<=11 and 1 in player_hand:
                player_score+=10
                
            
            #Dealer stays on all 17s
            if soft_score>=17:
                
                #If dealer bust, player wins bet
                if soft_score>21:
                    return bet, deck
                
                #If player has more than dealer, player wins bet
                if player_score>soft_score:
                    return bet, deck
                
                #Tie means no money changes hands
                if player_score==soft_score:
                    return 0, deck
                
                #If player has lower, player loses bet
                if player_score<soft_score:
                    return (0 - bet), deck
                

       
    
    if hard_stay==True:
        
        #Plays out only dealer's side, as player has to stop after 1 card
        
        while True:
            
            

                #Give dealer extra card if loop hasn't broken
            dealer_cards.append(deck[0])
            deck = np.delete(deck,0)
            
            
            #Keep track of sum of dealer's cards
            dealer_score= sum(dealer_cards)
            
            #Keep track of soft score if dealer has an ace
            
            soft_score= dealer_score
            if dealer_score<=11 and 1 in dealer_cards:
                soft_score+=10
                
            #If dealer gets blackjack you lose even if you have 21
            if len(dealer_cards)==2 and soft_score==21:
                return (0-bet), deck
                
            #Keeps track of player's score     
            player_score=sum(player_hand)
            
            #Uses soft score if that is better for player
            if player_score<=11 and 1 in player_hand:
                player_score+=10
                
            
            #Dealer stays on all 17s
            if soft_score>=17:
                
                #If dealer bust, player wins bet
                if soft_score>21:
                    return bet, deck
                
                #If player has more than dealer, player wins bet
                if player_score>soft_score:
                    return bet, deck
                
                #Tie means no money changes hands
                if player_score==soft_score:
                    return 0, deck
                
                #If player has lower, player loses bet
                if player_score<soft_score:
                    return (0 - bet), deck










### BLACKJACK SIMULATION ############
def blackjack_sim(n_hands=5, player_h='q', dealer_c='q', starting_bet=10, hard_c=4, num_decks = 6, shuffle_perc = 25):
    def new_deck(num_decks2 = num_decks):
        std_deck = [
		  # 2  3  4  5  6  7  8  9  10  J   Q   K   A
			2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
			2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            ]		# add more decks
        std_deck = std_deck * num_decks2

        random.shuffle(std_deck)
        std_deck = np.array(std_deck)
        return std_deck[:]
    deck_to_play = new_deck()


    ### incorporating the decks


    pnl=0
    #res=[]
    p=player_h
    q=len(player_h)
    bet2 = starting_bet
    for i in range(n_hands):
        #print("bet = ",bet2)
        hand_result, deck_to_play = blackjack_hand_result(bet=bet2, player_hand=p[:q], dealer_card=dealer_c, hard_code= hard_c, deck = deck_to_play)
        
        if (float(len(deck_to_play))/(52*num_decks))*100 < shuffle_perc:
            deck_to_play = new_deck()
        
        
        pnl = pnl + hand_result
        #print("result_multiplier= ",hand_result/bet2)
        #print("deck= ",deck_to_play)
        if (hand_result/bet2) != 1.5:
            bet2 = bet2 + 1
        else:
            bet2 = 5
        #print("hand_result = ", hand_result)
        #print("new_bet = ",bet2)
        #print("running_total =",pnl)
        
    return pnl


test = blackjack_sim(n_hands=100, starting_bet=5) 



blackjack_sim(n_hands=100, starting_bet=5) 




for i in range(5):
    results = blackjack_sim(n_hands=50, starting_bet=5) 
    print(results)
    
    
    
(blackjack_sim(n_hands=1_000_000, starting_bet=1))

#Simulates a million hands to estimate house edge
house_edge=-100*(blackjack_sim(n_hands=1_000_000, starting_bet=1) / 1_000_000)
house_edge #percentage



### just want to return the result of a single hand of blackjack 



blackjack_hand_result(bet=5)



#### need to figure out a way to incorporate the decks













#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 20:52:55 2025

@author: andrewczekay
Description: This program holds the functions required to play games of blackjack
"""

import random
import sys
import csv



# not sure if betting or some form or wagering will be included but populate this function if needed
def placeBet():
    wager = 0


# Creates the deck. Will be replaced by csv card inputs I assume
def createDeck():
    suits = ['H','D','S','C']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = []
    for i in range(len(suits)):
        for j in range(len(ranks)):
            card = (suits[i],ranks[j])
            deck.append(card)
    random.shuffle(deck)
    return deck

def shuffle(deck):
    with open(deck, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader) #convert into a list, easier to work with in python

        random.shuffle(rows) #shuffle all rows

        with open(deck, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)


# Pulls a card from the deck to deal. May be bypassed by inputting cards from the csv file
def dealCard(cards):
    card = cards.pop(0)
    return card


# Builds out the player and dealer hands. 
def buildHands(deckName):
    with open(deckName,"r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        cards = list(reader)

        playerHand = []
        dealerHand = []
        count = 0
        while count < 2:
            playerHand.append(tuple(dealCard(cards)))
            dealerHand.append(tuple(dealCard(cards)))
            count += 1
    with open(deckName, "w",newline="") as outfile: #deletes the 4 cards from the csv file
        writer = csv.writer(outfile)
        writer.writerows(cards)

    return tuple(playerHand), tuple(dealerHand)


# Calculates hand value totals; includes ace's 1/11 mechanic
def calculateHand(hand):
    total = 0
    numAces = 0
    for card in hand:
        cardRank = card[0]
        if cardRank.isdigit() == True:
            cardValue = int(cardRank)
            total += cardValue
        elif cardRank == 'J' or cardRank == 'Q' or cardRank == 'K':
            cardValue = 10
            total += cardValue
        elif cardRank == 'A':
            cardValue = 11
            total += cardValue
            numAces += 1
    
    #This block changes an ace value from 11 to 1 if it prevents a bust
    while total > 21 and numAces != 0:
        total -= 10
        numAces -= 1
    
    return total




def hit(deck,playerHand,dealerHand):
    playerHand.append(dealCard(deck))
    ptotal = calculateHand(playerHand)
    if ptotal > 21:
        print(f"Your hand is now {playerHand}, and its value is {ptotal}, which means you bust and lose!")
        sys.exit(-1)
    print(f"Your hand is {playerHand} and its value is {ptotal}")
    print(f"The dealer is showing {dealerHand[1]}")
    return playerHand, ptotal
    

def stand(deck,playerHand,dealerHand):
    global flag
    flag = 0
    dtotal = calculateHand(dealerHand)
    ptotal = calculateHand(playerHand)
    while dtotal < 17:
        dealerHand.append(dealCard(deck))
        dtotal = calculateHand(dealerHand)
        print(f"The dealer hits and their hand is now {dealerHand} and its value is {dtotal}")
    return playerHand, ptotal, dealerHand, dtotal


def result(playerHand, ptotal, dealerHand, dtotal):
    if dtotal > 21:
        print("The dealer busts and you win!")
    elif ptotal == 21 and dtotal != 21:
        print("Blackjack! You win!")
    elif dtotal > ptotal:
        print(f"The dealer has {dtotal} and you have {ptotal}, so you lose.")
    elif ptotal > dtotal:
        print(f"The dealer has {dtotal} and you have {ptotal}, so you win!")
    elif ptotal == 21 and dtotal == 21:
        print("Push! Its a tie, you both have blackjack.")
    elif ptotal == dtotal:
        print(f"Push! Its a tie, you both have {ptotal}.")
        
        
        

# Plays out one hand of blackjack each call

# Kept in for testing purposes as I split up into hit/stand/result funcs
def playRound():
    global flag
    flag = 1
    wager = placeBet()
    deck = createDeck()
    playerHand, dealerHand = buildHands(deck)
    ptotal = calculateHand(playerHand)
    print(f"Your hand is {playerHand} and its value is {ptotal}")
    print(f"The dealer is showing {dealerHand[1]}")

    while flag == 1:
        h_s = input("Would you like to hit or stand? (h/s): ")
        if h_s.lower() == "h":
            playerhand,ptotal = hit(deck,playerHand,dealerHand)
        elif h_s.lower() == "s":
            playerHand, ptotal, dealerHand, dtotal = stand(deck,playerHand,dealerHand)
    
    result(playerHand, ptotal, dealerHand, dtotal)
        
        
# playRound()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:19:15 2017

@author: dhingratul
"""
from fractions import gcd


def generateDeck(num_cards):
    """
    Generates and returns a card deck

    Input: num_cards: Number of cards in the card deck
    Output: Returns generated deck
    """
    deck = list(range(0, num_cards))
    return deck


def oneRound(deck):
    """
    Returns the card deck of size N after one "round", defined as follows:
    1. Take the top card off the deck and set it on the table
    2. Take the next card off the top and put it on the bottom of the deck in
    your hand.
    3. Continue steps 1 and 2 until all cards are on the table. This is a round

    Input: card deck
    Output: Card deck after one round
    """
    onTable = []
    while len(deck) > 0:
        onTable.append(deck.pop(0))  # One on the table
        if len(deck) != 0:
            deck.append(deck.pop(0))  # One at the bottom of deck
    onTable.reverse()  # Reversed to keep the correct order, as append was used
    return onTable


def numCycles(oneRoundDeck):
    """
    Determines the number of cycles betwen initial(from generateDeck(N) and the
    current configuration

    Input : Current configuration of deck
    Output: Returns the number of cycles
    """
    cycles = [1] * len(oneRoundDeck)
    for i in range(0, len(oneRoundDeck)):
        idx = i
        while oneRoundDeck[idx] != i:
            idx = oneRoundDeck[idx]
            cycles[i] += 1
    return cycles


def LCM(deck):
    """
    Determines the lcm of a given deck

    Input : deck
    Output: LCM of deck
    """
    lcm = 1
    for i in range(0, len(deck)):
        lcm = lcm * int(deck[i] / gcd(lcm, deck[i]))
    return lcm


def numRounds(deck):
    """
    Returns the number of rounds(N) required to obtain the originial order of
    deck, which is equivalent to runnning OneRound N times to obtain the
    original structure of deck

    Input: New deck from generateDeck
    Output: Number of rounds required to put back the deck in original order
    """

    deck_after_round_one = oneRound(generateDeck(deck))
    number_of_cycles = numCycles(deck_after_round_one)
    N = LCM(number_of_cycles)
    return N

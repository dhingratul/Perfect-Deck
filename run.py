#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:42:15 2017

@author: dhingratul
"""
import perfect_deck
import sys

if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
    deck_size = int(sys.argv[1])
    N = perfect_deck.numRounds(deck_size)
    print("{} cards --> {} Rounds".format(deck_size, N))
else:
    print("Correct Usage : \n  python run.py [size of deck > 0]")

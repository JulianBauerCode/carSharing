#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import os

# Expand path to module
mainDir = os.path.dirname(__file__)
sys.path.insert(0,
        os.path.abspath(
            os.path.join(mainDir,'..')))
del mainDir
import carSharingBills as cSB 

def test_compareImplementationsCalcPriceSingleRide():
    for distance in [0,1,10,100,200]:
        for duration in [0,1,10,24,50]:
            assert  cSB.calculatePriceOfSingleRide(distance, 
                        duration) \
                    == cSB.calculatePriceOfSingleRide2(distance,
                            duration)





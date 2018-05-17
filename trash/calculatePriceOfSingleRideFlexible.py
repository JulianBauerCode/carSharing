#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:33:20 2018

@author: me
"""

import math


def calculatePriceOfSingleRide2(distance, duration,
                                rates=(0.5, 0.28, 0.23),          # [Euro / km]
                                ratesStarts=(0, 50, 100),         # [km]
                                highDurationsPrices=(0, 25),      # [Euro]
                                highDurationsStarts=(-math.inf, 24),   # [h]
                                minPrice=0):                      # [Euro]

    """Calculate the price of one single ride based on parameter lists

    Parameters
    ----------
    distance : float
        Distance of the ride in kilometer
    duration : float
        Duration of the ride in hours
    rates : [floats]
        Rates specifying cost per distance starting from corresponding
        value of ratesStarts
    ratesStarts : [floats]
        Starting from this distances, the corresponding rates from rates
        is applied
    highDurationPrices : [floats]
        Minimum prices starting from corresponding value of
        highDurationsStarts
    highDurationsStarts : [floats]
        Starting from this distances, the corresponding prices from
        highDurationPrices is applied
    minPrice : float
        Minimum price

    Returns
    -------
    Float
        The price in Euro

    Raises
    ------
    None
    """
    import bisect

    # Calc temporary price based on distance
    indexDistance = bisect.bisect_left(ratesStarts, distance)
    price = minPrice
    for rateIndex in range(indexDistance - 1):
        price = price + rates[rateIndex]\
                * (ratesStarts[rateIndex + 1] - ratesStarts[rateIndex])
    price = price + rates[indexDistance - 1]\
        * (distance - ratesStarts[indexDistance - 1])

    # Calc minimum price based on duration
    minPriceDueToDuration = highDurationsPrices[
            bisect.bisect_right(
                highDurationsStarts, duration)-1]

    # Define minimum price based on duration
    return max(minPriceDueToDuration, price)

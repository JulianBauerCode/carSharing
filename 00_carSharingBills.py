#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:58:13 2018

@author: me
"""

import pandas as pd
import os
import datetime
import dateutil
import string
import subprocess
import locale

import sys
sys.path.append(os.path.join(os.getcwd(), 'source'))
import core

if (__name__ == '__main__'):
    pathMain = os.path.dirname(os.path.abspath('__file__'))
    pathLogbook = os.path.join(
            pathMain,
            '02_logbook.xlsx')
    pathTableOfDrivers = os.path.join(
            pathMain,
            '01_tableOfDrivers.xlsx')
    dirOutput = os.path.join(pathMain, 'output')

    m = core.BillManager(
                    year=2001,
                    month=1,
                    autoDate=True,
                    dateOfBill=None,
                    pathTableOfDrivers=pathTableOfDrivers,
                    pathLogbook=pathLogbook,
                    dirOutput=dirOutput
                    )
    m.createBills()

    m.plotPriceFunction()

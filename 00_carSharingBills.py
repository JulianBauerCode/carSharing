#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################
# Import main code
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'source'))
import core

################## ################## ##################
# Start user input

# Please insert the month and year of the month which should be processed
month = 1
year = 2001

##################
# Optional input:

# Please insert paths to 
#   01_tableOfDrivers.xlsx
#   02_lobook.xlsx
#   output-directory
# You can use relative paths starting at the directory where this script is located (pathMain)

# Path to directory of this script
pathMain = os.path.dirname(os.path.abspath('__file__'))

# Path to 01_tableOfDrivers.xlsx
pathLogbook = os.path.join(
        pathMain,
        '02_logbook.xlsx')

# Path to 02_lobook.xlsx
pathTableOfDrivers = os.path.join(
        pathMain,
        '01_tableOfDrivers.xlsx')

# Path to output-directory
dirOutput = os.path.join(
        pathMain,
        'output')

# End user input
################## ################## ##################

##################
# Call main code

m = core.BillManager(
                year=year,
                month=month,
                autoDate=True,
                dateOfBill=None,
                pathTableOfDrivers=pathTableOfDrivers,
                pathLogbook=pathLogbook,
                dirOutput=dirOutput,
                keepTexFiles=True,
                )
m.createBills()

#Uncomment the follwoing line to print cost-function
#m.plotPriceFunction()

import pandas as pd
import os

if __name__ == '__main__':
    # Define path to main directory
    path_main = os.path.dirname(os.path.abspath('__file__'))
    # Read logbook
    path_logbook = os.path.join(path_main, 'data', 'logbook.xlsx')
    logbook = pd.read_excel(io=path_logbook)
    # Access items
    logbook['dateEnd'].dt.date[0]
    logbook['timeEnd'][0]

    # Read table of drivers
    path_tableOfDrivers = os.path.join(path_main, 'data', 'tableOfDrivers.xlsx')
    tableOfDrivers = pd.read_excel(io=path_tableOfDrivers)

    # Read dictionary
    path_dictionary = os.path.join(path_main, 'data', 'dictionary.xlsx')
    dictionary = pd.read_excel(io=path_dictionary)














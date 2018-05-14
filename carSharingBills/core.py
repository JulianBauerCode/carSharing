import pandas as pd
import os

if __name__ == '__main__':
    ##################
    # Read data

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

    ##################
    # Combine columns to datetime objects
    # https://stackoverflow.com/a/39474812/8935243

    logbook['start'] = logbook.apply( 
                        func = lambda r: 
                            pd.datetime.combine(r['dateStart'], r['timeStart']),
                        axis = 1)

    logbook['end'] = logbook.apply( 
                        func = lambda r: 
                            pd.datetime.combine(r['dateEnd'], r['timeEnd']),
                        axis = 1)

    ##################
    # Calc duration
    
    logbook['duration'] = logbook.apply(
                        func = lambda r:
                            ((r['end']-r['start']).total_seconds())/(60*60),
                            # unit = hours
                        axis = 1)








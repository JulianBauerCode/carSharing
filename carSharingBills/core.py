import pandas as pd
import os
import datetime
import dateutil

def calculatePriceOfSingleRide(distance, duration):
    """Calculate the price of one single ride
    
    Adjust this function to the needs of your pricing structure.
    
    If the duration of the ride is larger than \"highDuration\",
    the price of the ride is at least \"minPriceHighDuration\".

    Prices per kilometer decrease in two steps from rate1, over rate2 
    to rate3.
    rate1 applies to kilometers from zero up to \"maxDistanceForRate1\".
    rate2 applies to kilometers from \"maxDistanceForRate1\" 
    up to \"maxDistanceForRate2\".
    rate3 applies to all kilometers up from \"maxDistanceForRate2\".

    Args:
        distance: Distance of the ride in kilometer
        duration: Duration of the ride in hours

    Returns:
        Float representing the price in Euro
    
    Raises:
        None
    
    """

    highDuration            = 24 #[h]
    minPriceHighDuration    = 25 #[Euro]

    rate1 = 0.5    #[Euro / km]
    rate2 = 0.28   #[Euro / km]
    rate3 = 0.23   #[Euro / km]
    maxDistanceForRate1 = 50  #[km]
    maxDistanceForRate2 = 100 #[km]

    # Calc temporary price based on distance
    if(distance <= maxDistanceForRate1 ):
        tmpPrice = distance * rate1
    elif(distance <= maxDistanceForRate2):
        tmpPrice = maxDistanceForRate1 * rate1 +\
            (distance - maxDistanceForRate1) * rate2
    else:
        tmpPrice = maxDistanceForRate1 * rate1 +\
            (maxDistanceForRate2 - maxDistanceForRate1) * rate2 +\
            (distance - maxDistanceForRate2) * rate3

    # Ensure minimum price if duration is high
    if(highDuration <= duration):
        price = max( [tmpPrice , minPriceHighDuration] )
    else:
        price = tmpPrice

    return price

class DriverUnknown(Exception):
    """Driver is unknown, i.e. driver is not in table of drivers"""
    pass

if __name__ == '__main__':
    year = 2001
    month = 1
    
    ##################
    # Read data

    # Define path to main directory
    path_main = os.path.dirname(os.path.abspath('__file__'))

    # Read logbook
    path_logbook = os.path.join(path_main, 'data', 'logbook.xlsx')
    logbook = pd.read_excel(io=path_logbook)

    # Read table of drivers and set index
    path_tableOfDrivers = os.path.join(
            path_main,
            'data',
            'tableOfDrivers.xlsx')
    tableOfDrivers = pd.read_excel(io=path_tableOfDrivers)\
            .set_index('driver')

    # Read dictionary and convert into python-dict
    path_dictionary = os.path.join(
            path_main,
            'data',
            'dictionary.xlsx')
    dictionary = pd.read_excel(
            io=path_dictionary,
            header = None,
            skiprows = 1)
    dictionary = dictionary.set_index(0).to_dict()[1]

    ##################
    # Combine pairs of date and time to datetime objects
    # https://stackoverflow.com/a/39474812/8935243

    logbook['start'] = logbook.apply( 
                        func = lambda row: 
                            pd.datetime.combine(
                                row['dateStart'],
                                row['timeStart']),
                        axis = 1)

    logbook['end'] = logbook.apply( 
                        func = lambda row: 
                            pd.datetime.combine(
                                row['dateEnd'],
                                row['timeEnd']),
                        axis = 1)

    ##################
    # Calc duration
    
    logbook['duration'] = logbook.apply(
                        func = lambda row:
                            ((row['end']-row['start'])\
                                    .total_seconds())/(60*60),
                            # unit = hours
                        axis = 1)

    ##################
    # Calc price

    logbook['price'] = logbook.apply(
                        func = lambda row:
                            calculatePriceOfSingleRide(
                                distance = row['distance'],
                                duration = row['duration']),
                        axis = 1)

    ##################
    # Filter data for time range

    # Define start of month
    start = datetime.datetime(year = year, month = month, day = 1)
    # Define end of month
    end = start + dateutil.relativedelta.relativedelta(
            months          = +1,
            microseconds    = -1)

    # Filter and set index
#.sort_index(level=['year','foo'], ascending=[1, 0], inplace=True)
    logbookF = logbook.set_index('start')
    logbookF.sort_index(inplace=True)
    logbookF = logbookF.loc[start:end].reset_index()

    ##################
    # Calc total price for each driver

    totalPrice = logbookF.groupby(['driver'])['price'].sum()

    ##################
    # Create list of active drivers

    activeDrivers = totalPrice.index.tolist()

    ##################
    # Check if all active driver are in table of drivers

    for driver in activeDrivers:
        if driver not in tableOfDrivers.index:
            raise DriverUnknown(
                'Driver \"{}\"'.format(driver) \
                + 'is not found in table of drivers:\n' \
                + '{}'.format(tableOfDrivers))
          


















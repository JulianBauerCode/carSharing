import pandas as pd
import os
import datetime
import dateutil
import string
import subprocess
import locale

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

class UnSupportedOperatingSystem(Exception):
    """Operating system is not supported"""
    pass

class LatexTemplate(string.Template):
    """String template with special delimiter"""
    delimiter = "##"

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def createPdf(dirOutput, nameLatexFile, template, latexDict, 
        unnecessaryFileEndings ):

    pathLatexFile = os.path.join(dirOutput, nameLatexFile)
    with open( pathLatexFile, 'w' ,newline = '\n') as latexFile:
        latexFile.write(template.substitute(**latexDict))
    with cd(dirOutput):
        cmd = ['pdflatex',
                '-interaction',
                'nonstopmode',
                pathLatexFile]
        # Execute Latex two times to get total number of pages
        for i in range(2):  
            # Start process
            proc = subprocess.Popen(cmd)
            # Wait till process is finished
            out = proc.communicate()
        for ending in unnecessaryFileEndings:
            try:
                os.unlink(os.path.splitext(pathLatexFile)[0]
                            + ending)
            except:
                     pass
    return None

def monthGerman(integerMonth):
    """Return German name of month"""    
    gerMonthsNamesList = ['Januar', 'Februar', 'März' ,'April', 
           'Mai','Juni','Juli','August','September','Oktober',
           'November','Dezember']
    if (1 <= integerMonth) & (integerMonth <=12):
        month = gerMonthsNamesList[integerMonth-1]
    else:
        raise ValueError(
                'Integer specifying month has to be in [1,12]'\
                        '\n can\' process integer {}'.format(
                            str(integerMonth)))
    return month

def getTemplate(pathTemplate):
    """Get latex template"""
    with open(pathTemplate,'r', newline='') as myFile:
        template = LatexTemplate(myFile.read())
    return template

def renameDataFrameIndexNames(dataFrame, dictionary):
    """Rename index names of data frame object inplace"""
    length = len(dataFrame.index.names)
    if length == 1:
         dataFrame.index.rename(
            dictionary[dataFrame.index.name],
            inplace = True) 
    else:
         dataFrame.index.rename(
            [dictionary[name] for name in dataFrame.index.names],
            inplace = True)
    return dataFrame

if __name__ == '__main__':

    year = 2001
    month = 1
    automaticDate = True

    ##################
    # Define settlement date
    if automaticDate:
        if os.name == 'posix':#We ware on Linux
            locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') 
            settlementDate = datetime.datetime.now().strftime(
                    "%-d. %B %Y")
        elif os.name ==  'nt':#We are on Windows
            locale.setlocale(locale.LC_ALL, 'deu_deu')
            settlementDate = datetime.now().strftime("%#d. %B %Y")
        else:
            raise UnSupportedOperatingSystem(
                    'The operating system is neither \'posix = Linux\''\
                    'nor  \'nt = Windows\'.\n'\
                    'The local format of the settlement date can\'t be'\
                    'determined automatically.\n Please insert it'\
                    'by Hand')

    ##################
    # Read data

    # Define path to main directory
    pathMain = os.path.dirname(os.path.abspath('__file__'))

    # Read logbook
    pathLogbook = os.path.join(pathMain, 'data', 'logbook.xlsx')
    logbook = pd.read_excel(io=pathLogbook)

    # Read table of drivers and set index
    pathTableOfDrivers = os.path.join(
            pathMain,
            'data',
            'tableOfDrivers.xlsx')
    tableOfDrivers = pd.read_excel(io=pathTableOfDrivers)\
            .set_index('driver')

    # Read dictionary and convert into python-dict
    pathDictionary = os.path.join(
            pathMain,
            'data',
            'dictionary.xlsx')
    dictionary = pd.read_excel(
            io=pathDictionary,
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
    logbookF = logbook.set_index('start')
    logbookF.sort_index(inplace=True)
    logbookF = logbookF.loc[start:end].reset_index()

    ##################
    # Calc total price for each driver

    grouped = logbookF.groupby(['driver'])
    totalDuration   = grouped['duration'].sum()
    totalDistance   = grouped['distance'].sum()
    totalPrice      = grouped['price'].sum()

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
          
    ##################
    # Create overview latex tables

    overview =  logbookF.set_index(['driver', 'car'])[
                               ['start',
                                'end',
                                'duration',
                                'distance',
                                'price']]
    summation = pd.DataFrame(
            [   totalDistance, 
                totalDuration,
                totalPrice]).T

    ##################
    # Rename overview latex tables

    overviewRenamed = overview.rename(columns = dictionary)
    overviewRenamed = renameDataFrameIndexNames(
            overviewRenamed, dictionary)
    
    dictionarySummation = {
            key: dictionary['total']+' '+value 
            for key,value in dictionary.items()}
    summationRenamed = summation.rename(columns = dictionarySummation)
    summationRenamed = renameDataFrameIndexNames(
            summationRenamed, dictionarySummation)


    ##################
    # Wrap tables in dict

    overviewDict = {}
    overviewDict['overviewTable']   = overviewRenamed.to_latex()
    overviewDict['summationTable']  = summationRenamed.to_latex()

    ##################
    # Create output directory

    dirOutput = os.path.join( pathMain, 'output' )
    if not os.path.exists(dirOutput):
        os.makedirs(dirOutput)
 
    ##################
    # Define unnecessary file endings which will be deleted

    unnecessaryFileEndings = ['.aux','.log']

    ##################
    # Process overview

    # Define name
    nameLatexFile = '{y}_{m}_{name}.tex'.format(
                y = str(year),
                m = str(month).zfill(2),
                name = 'overview')

    # Excute
    createPdf(dirOutput = dirOutput,
              nameLatexFile = nameLatexFile,
              template = getTemplate(pathTemplate = os.path.join(
                            pathMain,
                            'templates',
                            'overview.tex')),
              latexDict = overviewDict,
              unnecessaryFileEndings = unnecessaryFileEndings)

    ##################
    # Process drivers
   
    keys = ['firstName', 'lastName', 'street', 'streetNumber',
                'postCode', 'city']

    driverDicts = {}
    for driver in activeDrivers:
        driverDict = {}
        driverDict['settlementDate'] = settlementDate
        driverDict['month'] = monthGerman(month) 
        driverDict['year']  = str(year)
        driverDict['table'] = overviewRenamed.loc[driver,:].to_latex()
        driverDict['totalPrice'] = str(totalPrice[driver]) + ' Euro'
        driverDict['pathSignature'] = os.path.relpath(
                path = os.path.join(pathMain, 'templates','signature'),
                start = dirOutput)
        for key in keys:
            driverDict[key] = tableOfDrivers.loc[driver][key]
        # Add current dict to dict of dicts
        driverDicts[driver] = driverDict 

    # Excute
    for driver in activeDrivers:
        createPdf(  dirOutput = dirOutput,
                    nameLatexFile = '{y}_{m}_{driver}.tex'.format(
                        y = str(year),
                        m = str(month).zfill(2),
                        driver = driver),
                    template = getTemplate(
                        pathTemplate = os.path.join(
                            pathMain,
                            'templates',
                            'singleUser.tex')),
                    latexDict = driverDicts[driver],
                    unnecessaryFileEndings = unnecessaryFileEndings)











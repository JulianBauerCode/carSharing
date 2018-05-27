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

    Parameters
    ----------
    distance : float
        Distance of the ride in kilometer
    duration : float
        Duration of the ride in hours

    Returns
    -------
    Float
        The price in Euro

    Raises
    ------
    None
    """

    highDuration = 24           # [h]
    minPriceHighDuration = 25   # [Euro]

    rate1 = 0.5    # [Euro / km]
    rate2 = 0.28   # [Euro / km]
    rate3 = 0.23   # [Euro / km]
    maxDistanceForRate1 = 50    # [km]
    maxDistanceForRate2 = 100   # [km]

    # Calc temporary price based on distance
    if(distance <= maxDistanceForRate1):
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
        price = max([tmpPrice, minPriceHighDuration])
    else:
        price = tmpPrice

    return price


class BillManager():
    """Processes one single month"""
    def __init__(self, year, month, pathLogbook, pathTableOfDrivers,
                 pathDictionary,
                 dirOutput,
                 priceOfSingleRide=calculatePriceOfSingleRide,
                 autoDate=True, dateOfBill=None):
        self.year = year
        self.month = month
        self.dateOfBill = self.getBillDateGerman(autoDate=autoDate,
                                                 dateOfBill=dateOfBill)
        self.pathLogbook = pathLogbook
        self.pathTableOfDrivers = pathTableOfDrivers
        self.pathDictionary = pathDictionary
        self.priceOfSingleRide = priceOfSingleRide
        self.dirOutput = dirOutput
        self.pathMain = os.path.dirname(os.path.abspath('__file__'))

    def createBills(self):

        # Read logbook
        self.logbook = pd.read_excel(io=self.pathLogbook)

        # Read table of drivers and set index
        self.tableOfDrivers = pd.read_excel(io=self.pathTableOfDrivers)\
            .set_index('driver')

        # Read dictionary and convert into python-dict
        self.dictionary = pd.read_excel(
                io=self.pathDictionary,
                header=None,
                skiprows=1)
        self.dictionary = self.dictionary.set_index(0).to_dict()[1]

        ##################
        # Combine pairs of date and time to datetime objects
        # https://stackoverflow.com/a/39474812/8935243

        self.logbook['start'] = self.logbook.apply(
                            func=lambda row:
                            pd.datetime.combine(
                                row['dateStart'],
                                row['timeStart']),
                            axis=1)

        self.logbook['end'] = self.logbook.apply(
                            func=lambda row:
                            pd.datetime.combine(
                                row['dateEnd'],
                                row['timeEnd']),
                            axis=1)

        ##################
        # Filter data for time range

        # Define start of month
        self.start = datetime.datetime(year=self.year,
                                          month=self.month,
                                          day=1)

        # Define end of month
        self.end = self.start + dateutil.relativedelta.relativedelta(
                                                    months=+1,
                                                    microseconds=-1)

        # Filter and set index
        self.logbookF = self.logbook.set_index('start')
        self.logbookF.sort_index(inplace=True)
        self.logbookF = self.logbookF.loc[self.start:self.end]\
            .reset_index()

        ##################
        # Calc duration

        self.logbookF['duration'] = self.logbookF.apply(
                                func=lambda row:
                                ((row['end']-row['start'])
                                    .total_seconds())/(60*60),
                                # unit = hours
                                axis=1)

        ##################
        # Calc price

        self.logbookF['price'] = self.logbookF.apply(
                            func=lambda row:
                            self.priceOfSingleRide(
                                distance=row['distance'],
                                duration=row['duration']),
                            axis=1)

        ##################
        # Calc total price for each driver

        self.grouped = self.logbookF.groupby(['driver'])
        self.totalDuration = self.grouped['duration'].sum()
        self.totalDistance = self.grouped['distance'].sum()
        self.totalPrice = self.grouped['price'].sum()

        ##################
        # Create list of active drivers

        self.activeDrivers = self.totalPrice.index.tolist()

        ##################
        # Check if all active driver are in table of drivers

        for driver in self.activeDrivers:
            if driver not in self.tableOfDrivers.index:
                raise DriverUnknown(
                    'Driver \"{}\"'.format(driver)
                    + 'is not found in table of drivers:\n'
                    + '{}'.format(self.tableOfDrivers))

        ##################
        # Create overview latex tables

        self.overview = self.logbookF.set_index(['driver', 'car'])[[
                                    'start',
                                    'end',
                                    'duration',
                                    'distance',
                                    'price']]
        self.summation = pd.DataFrame([
                        self.totalDistance,
                        self.totalDuration,
                        self.totalPrice]).T

        ##################
        # Change format of datetimes
        self.format = '%Y-%m-%d %H:%M'
        for label in ['start', 'end']:
            self.overview[label] = self.overview[label].dt.strftime(
                self.format)

        ##################
        # Rename overview latex tables

        self.overviewR = self.overview.rename(columns=self.dictionary)
        self.overviewR = self.renameDataFrameIndexNames(
                self.overviewR, self.dictionary)

        self.dictionarySummation = {
                key: self.dictionary['total']+' '+value
                for key, value in self.dictionary.items()}
        self.summationR = self.summation.rename(
                columns=self.dictionarySummation)
        self.summationR = self.renameDataFrameIndexNames(
                self.summationR, self.dictionarySummation)

        ##################
        # Wrap tables in dict

        self.overviewDict = {}
        self.overviewDict['overviewTable'] =\
            self.overviewR.to_latex()
        self.overviewDict['summationTable'] =\
            self.summationR.to_latex()

        ##################
        # Create output directory

        if not os.path.exists(self.dirOutput):
            os.makedirs(self.dirOutput)

        ##################
        # Define unnecessary file endings which will be deleted

        self.unnecessaryFileEndings = ['.aux', '.log']

        ##################
        # Process overview

        # Define name
        self.nameLatexFile = '{y}_{m}_{name}.tex'.format(
                    y=str(self.year),
                    m=str(self.month).zfill(2),
                    name='overview')

        # Excute
        self.createPdf(dirOutput=self.dirOutput,
                       nameLatexFile=self.nameLatexFile,
                       template=self.getTemplate(
                                       pathTemplate=os.path.join(
                                               self.pathMain,
                                               'templates',
                                               'overview.tex')),
                       latexDict=self.overviewDict,
                       unnecessaryFileEndings=
                           self.unnecessaryFileEndings)

        ##################
        # Process drivers

        keys = ['firstName', 'lastName', 'street', 'streetNumber',
                'postCode', 'city']

        self.driverDicts = {}
        for driver in self.activeDrivers:
            driverDict = {}
            driverDict['dateOfBill'] = self.dateOfBill
            driverDict['month'] = self.monthGerman(self.month)
            driverDict['year'] = str(self.year)
            driverDict['table'] = self.overviewR.loc[driver, :]\
                .to_latex()
            driverDict['totalPrice'] = str(self.totalPrice[driver])\
                + ' Euro'
            driverDict['pathSignature'] = os.path.relpath(
                    path=os.path.join(pathMain, 'templates', 'signature'),
                    start=dirOutput)
            for key in keys:
                driverDict[key] = self.tableOfDrivers.loc[driver][key]
            # Add current dict to dict of dicts
            self.driverDicts[driver] = driverDict

        # Excute
        for driver in self.activeDrivers:
            self.createPdf(dirOutput=self.dirOutput,
                           nameLatexFile='{y}_{m}_{driver}.tex'.format(
                                  y=str(self.year),
                                  m=str(self.month).zfill(2),
                                  driver=driver),
                           template=self.getTemplate(
                                pathTemplate=os.path.join(
                                    self.pathMain,
                                    'templates',
                                    'singleUser.tex')),
                           latexDict=self.driverDicts[driver],
                           unnecessaryFileEndings=
                              self.unnecessaryFileEndings)

    def getBillDateGerman(self, autoDate, dateOfBill):
        if autoDate:
            if os.name == 'posix':  # We are on Linux
                locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
                dateOfBill = datetime.datetime.now().strftime(
                        "%-d. %B %Y")
            elif os.name == 'nt':  # We are on Windows
                locale.setlocale(locale.LC_ALL, 'deu_deu')
                dateOfBill = datetime.now().strftime("%#d. %B %Y")
            else:
                raise UnSupportedOperatingSystem(
                        'The operating system is neither \'posix = Linux\''
                        'nor  \'nt = Windows\'.\n'
                        'The local format of the bills date can\'t be'
                        'determined automatically.\n Please insert it'
                        'by Hand')
        return dateOfBill

        def plotPriceFunction(self, dictionary,
                              function=calculatePriceOfSingleRide,
                              rangeDistance=[0, 120],
                              rangeDuration=[0, 50],
                              ylim=[0, 45]):
            import numpy as np
            # %matplotlib auto
            # import matplotlib
            # matplotlib.rcParams.update({'font.size': 22})
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = fig.add_subplot(111)

            for plotNumber, duration in enumerate([2, 24, 30]):
                ax.set_title('Variable distance, different durations')
                x = np.arange(*rangeDistance)
                y = list(map(lambda x: function(
                    distance=x,
                    duration=duration), x))
                ax.plot(x, y,
                        label='Duration = {}'.format(duration),
                        linewidth=12 - 4 * plotNumber)

            ax.grid(True)
            ax.set_xlabel('distance')
            ax.set_ylabel('price')
            ax.set_ylim(*ylim)
            plt.legend()
            plt.show()

    def createPdf(self, dirOutput, nameLatexFile, template, latexDict,
                  unnecessaryFileEndings):

        pathLatexFile = os.path.join(dirOutput, nameLatexFile)
        with open(pathLatexFile, 'w', newline='\n') as latexFile:
            latexFile.write(template.substitute(**latexDict))
        with cd(dirOutput):
            cmd = ['pdflatex',
                   '-interaction',
                   'nonstopmode',
                   pathLatexFile]
            # Execute Latex two times to get total number of pages
            for i in range(2):
                # Start process
                proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
                # Wait till process is finished
                proc.communicate()
            for ending in unnecessaryFileEndings:
                try:
                    os.unlink(os.path.splitext(pathLatexFile)[0]
                              + ending)
                except(FileNotFoundError):
                    pass
        return None

    def monthGerman(self, integerMonth):
        """Return German name of month"""
        gerMonthsNamesList = ['Januar', 'Februar', 'März', 'April',
                              'Mai', 'Juni', 'Juli', 'August', 'September',
                              'Oktober', 'November', 'Dezember']
        if (1 <= integerMonth) & (integerMonth <= 12):
            month = gerMonthsNamesList[integerMonth-1]
        else:
            raise ValueError(
                    'Integer specifying month has to be in [1,12].'
                    '\n Can\'t process integer {}'.format(str(integerMonth)))
        return month

    def getTemplate(self, pathTemplate):
        """Get latex template"""
        with open(pathTemplate, 'r', newline='') as myFile:
            template = LatexTemplate(myFile.read())
        return template

    def renameDataFrameIndexNames(self, dataFrame, dictionary):
        """Rename index names of data frame object inplace"""
        length = len(dataFrame.index.names)
        if length == 1:
            dataFrame.index.rename(
                dictionary[dataFrame.index.name],
                inplace=True)
        else:
            dataFrame.index.rename(
                [dictionary[name] for name in dataFrame.index.names],
                inplace=True)
        return dataFrame


if (__name__ == '__main__'):
    pathMain = os.path.dirname(os.path.abspath('__file__'))
    pathLogbook = os.path.join(pathMain, 'data', 'logbook.xlsx')
    pathTableOfDrivers = os.path.join(
            pathMain,
            'data',
            'tableOfDrivers.xlsx')
    pathDictionary = os.path.join(
            pathMain,
            'data',
            'dictionary.xlsx')
    dirOutput = os.path.join(pathMain, 'output')

    m = BillManager(year=2001,
                    month=1,
                    pathLogbook=pathLogbook,
                    pathTableOfDrivers=pathTableOfDrivers,
                    pathDictionary=pathDictionary,
                    dirOutput=dirOutput,
                    priceOfSingleRide=calculatePriceOfSingleRide,
                    autoDate=True, dateOfBill=None)
    m.createBills()

# Installation
## Linux
    - Install Latex 
        - sudo apt-get install texlive texlive-lang-german texlive-doc-de texlive-latex-extra
    - Install Python3.6
        - sudo apt-get install python3.6
    - Clone this directoy
        - Download manually or
        - git clone https://github.com/JulianBauerCode/carSharing.git

## Windows
    - Install Latex
        - Download and install Miktex 2.9.6361 or newer and allow automatic installation of additional packages
        - Miktex can be found here: https://miktex.org/download
    - Install Python3.6 using Anaconda
        - Download from https://www.anaconda.com/download/#download and install
    - Clone this directory.
        - Download manually
        - Unzip

*Click on 'Clone or download' then click on 'Download Zip'*

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/download.png)

# Usage

## Start creating bills by executing the script
    - Start a terminal / ipython-console / spyder
    - Navigate to the cloned directory (path, where the script '00_carSharingBills.py' is located)
    - Execute the script '00_carSharingBills.py'
    - Look at output-directory

*Linux Terminal*

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/start.png)

*Ipython-Console*

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/complete.png)

*Spyder*

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/spyder.png)

## Do this each month

#### Update table of drivers
Insert new data using Excel or LibreOffice-Calc.

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/tableOfDrivers.png)

#### Update logbook
Insert new data using Excel or LibreOffice-Calc.
You decide whether you like to keep different files for different months or combine all the data in one single large Excel-file.
Python reads the complete file and filters the data in order to process the specified month.
A ride belongs to a specfified month, if the ride starts during this month.
This, for example,  means that all rides belonging to June start during June but may end in July.

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/logbook.png)

Bills are created monthly.
The next section demonstrated how to select the month, which is getting processed.

#### Select year and month
Open the file 00_carSharingBills.py and insert the month and year of the month you would like to process.

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/changeMonth.png)

Users, experienced in scripting, may adjust this script:

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/advanced.png)

#### Execute the script again

See above.

## Do the following once

You can specify

    - the layout of the bills
    - the signature inserted into the bills
    - the layout of the overview pdf
    - and the language used in the tables, generated by the script.

Each action requires manipulation of one file in the subdirectory "templates".

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/structure.png)


#### Change layout of the bills

Supply a compilable Latex-document with the following placeholders:

    - ##firstName
    - ##lastName
    - ##street
    - ##streetNumber
    - ##postCode
    - ##city
    - ##dateOfBill
    - ##month
    - ##year
    - ##table
    - ##totalPrice
    - ##pathSignature

Example:

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/exampleSingleUser.png)

#### Change the signature

Use your own one only.
Save a picture of your signature here:

*templates/signature.png*

#### Change template of overview pdf

Supply a compilable Latex-document with the following placeholders:

    - ##overviewTable
    - ##summationTable

Example:

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/exampleOverview.png)

#### Change dictionary / language

Python formats the calculated data into tables and passes these tables to the latex-templates.
You can specify the labels of these tables by manipulating the content of the file dictionary.xlsx.

![alt text](https://raw.githubusercontent.com/JulianBauerCode/pictures/master/carSharing/dictionary.png)


















<!--
# Create an environment:
#conda create --name car6 python=3.6
# Active the environment:
source activate template
# Create requirements.txt:
conda list --explicit > requirements.txt
# Create environment from requirements.txt:
#conda env create template2 --file requirements.txt
-->

from datetime import datetime

import pandas
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import csv
import xlrd




class Stock:

    def __init__(self, filename):
        '''Initialises a stock and allokates it with the apropriate data'''

        #get yearly data
        self.filename = '/Users/Niklas/Desktop/test.csv'
        self.yearlyStockDataFromCsvFile = {}
        #self.fetchYearlyStockDataFromCsvFile( self.filename)

        #get pricedata
        self.priceData = {}
        #self.fetchPriceOfStock(filename)

        self.yearlyStockDataFromXlsFile = {}
        self.fetchYearlyStockDataFromXlsFile('/Users/Niklas/Desktop/Borsdata/YearData/' + filename + ".xls")



    def fetchYearlyStockDataFromXlsFile(self, filename):
        '''Goes to the document for yearly stock data and fetches the content'''
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)


        # Make array containing dates
        tmp = []
        for col in range(2, sheet.ncols):
            element = sheet.row(0)[col]
            if "Q" in element.value:
                if element.value[1] is "1":
                    date = datetime(int(element.value[3:]), 4, 1)
                if element.value[1] is "2":
                    date = datetime(int(element.value[3:]), 7, 1)
                if element.value[1] is "3":
                    date = datetime(int(element.value[3:]), 10, 1)
                if element.value[1] is "4":
                    date = datetime(int(element.value[3:])+1, 1, 1)

                tmp.append(date)
            else:
                date = datetime(int(element.value),12,31)
                tmp.append(date)
        self.yearlyStockDataFromXlsFile["Dates"] = tmp


        #Make arrays containing datasets
        for row in range(1, sheet.nrows):
            tmp = []
            for col in range(0, sheet.ncols):
                if col != 0 and col!=1:
                    element = sheet.row(row)[col]
                    if isinstance(element.value, str):
                        tmp.append(np.nan)
                    else:
                        tmp.append(element.value)
            self.yearlyStockDataFromXlsFile[sheet.row(row)[0].value] = tmp #+ '(' + sheet.row(row)[1].value + ')']= tmp    #TODO handle different currencies in meaningful way





    def fetchPriceOfStock(self, filename):
        '''Goes to the appropriate xls file and
        reads the price data for that particular stock'''

        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)

        for col in range (0,sheet.ncols):
            tmp = []
            for row in range (1,sheet.nrows):
                element = sheet.row(row)[col]
                if element.ctype == xlrd.XL_CELL_DATE:
                    # Returns a tuple.
                    dt_tuple = xlrd.xldate_as_tuple(element.value, workbook.datemode)
                    # Create datetime object from this tuple.
                    get_col = datetime(
                        dt_tuple[0], dt_tuple[1], dt_tuple[2],
                        dt_tuple[3], dt_tuple[4], dt_tuple[5]
                    )
                    if row == 1:
                        self.stopdate = get_col
                    if row == sheet.nrows-1:
                        self.startdate = get_col
                    tmp.append(get_col)
                else:
                    tmp.append(element.value)
            self.priceData[sheet.row(0)[col].value] = tmp


'''    def getMovingAverage(self, timeStep):

        tmp = []
        data = []
        dates = []
        for i in range(timeStep, self.data.Close.shape[0]):
            print(self.data.Close[i])
            if len(tmp) == timeStep or i == len(self.data.Close)-1:
                data.append(np.mean(tmp))
                tmp = [self.data.Close[i]]
                dates.append(self.data.axes[0][i])
            else:
                tmp.append(self.data.Close[i])
        print('dates')
        print(len(dates))
        print(dates)
        print('data')
        print(len(data))
        print(data)
        print('out')
        print(pandas.DataFrame(data,columns = dates))
        return dates#{'dates':dates,'data':data }
'''


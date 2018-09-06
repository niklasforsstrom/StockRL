from datetime import datetime
from datetime import timedelta

import pandas
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

class Stock:


    def __init__(self, start, end, name):
        yf.pdr_override()
        self.start = start
        self.end = end
        self.name = name
        print("hej")

        self.data = pdr.get_data_yahoo(start=self.start, end=self.end, tickers=self.name, actions=true)
        
        
        

    def getYearlyStockDataFromCsvFile(self, completeFileName):
        ''' reads data from csv file of specific stock.
         The file can not contain å,ä,ö.
        '''
        self.yearlyStockDataFromCsvFile = {}
        with open(completeFileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            #Read all rows in the file
            for line_count, row in enumerate(csv_reader):
                if row[0] is not "":
                    # Prep work (altering the data to avoid errors when reading)
                    for index, word in enumerate(row):
                        if "," in word:
                            row[index] = word.replace(",",".")
                        if word is "":
                            row[index] = 'nan'
                            print(str(row))

                    #Get the names of the years on the first row, skip then last entry since its not just a number
                    if line_count == 0:
                        self.yearlyStockDataFromCsvFile['dates'] = [float(row[2]), float(row[3]), float(row[4]),
                                                  float(row[5]), float(row[6]), float(row[7]), float(row[8]),
                                                  float(row[9]), float(row[10])]
                        line_count += 1
                    #Name each row by a combination of first and second entry
                    #Store the following floats in an array
                    else:
                        try:
                            self.yearlyStockDataFromCsvFile[row[0] + "(" + row[1] + ")"] = [float(row[2]), float(row[3]), float(row[4]),
                                                                          float(row[5]), float(row[6]), float(row[7]),
                                                                          float(row[8]), float(row[9]), float(row[10])]
                        #if some value is not a proper float
                        except ValueError:
                            print('error on row: ' + str(line_count) + '. The row looks like the following: ' + str(row))
                        line_count += 1

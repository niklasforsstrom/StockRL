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
        
        
        
      def momentum(self, daysForw): #Ger lista/array med momentum för en aktie i månadsintervall
        close = []
        momentum = []
        day = 0
        current = self.start
        diff = timedelta(days=daysForw)
        future = self.start + diff
        while future <= self.end:
        	current = current + 1
        	future = current + diff
        	day = day + 1
        	close.append(self.data.iat[day, df.columns.get_loc('Close')])
        for i in range(0, len(close)-daysForw): #Blir detta rätt med index?
            momentum.append(((close[i+daysForw]-close[i])/close[i])*100) #tänk på att första värdet inte får ngt momentum, ger det i procentutveckling

            
      def getYearlyStockDataFromCsvFile(self, completeFileName):
        # reads data from csv file of specific stock.
        # The file can not contain å,ä,ö.
        # The file can not have empty rows
        # the file cant have empty cells
        # decimal values need to be written with . not ,
        
        self.yearlyStockDataFromCsvFile = {}
        with open(completeFileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            #Read all rows in the file
            for row in csv_reader:
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
                        print('error on row: ' + line_count + '. The row looks like the following: ' + row)
                    line_count += 1

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
        
        
   
        
   

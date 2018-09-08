

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
import datetime
import DataHandler as dh
from Stock import Stock


def getMomentum(index, dataFrame, timeStep = 10):
    #TODO fix this method
    pass

def getPE():
    #TODO
    pass

def removeIndex(stock):
    pass
    #if (index == null):
    #   index = createIndex()
    #return stock.High - index.High

def createIndex(start, end):
    index = pdr.get_data_yahoo("^OMX", start=datetime.datetime(1991,7,21), end=datetime.datetime(20123,1,1))

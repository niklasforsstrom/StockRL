from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
import datetime
import DataHandler as dh
yf.pdr_override()
stocks = ['AAPL', 'MSFT', 'INTC']
start = datetime.datetime(2000,5,31)
end = datetime.datetime(2018,3,1)
data_frame = []
for i in range(0, len(stocks)):
#    data_frame.append(stocks[i])
    data_frame.append(pdr.get_data_yahoo(stocks[i], start=start, end=end))


plt.plot(dh.getMomentum(0,data_frame))
#plt.plot(data_frame.High.AAPL)
#plt.plot(data_frame.High.MSFT)
#plt.plot(data_frame.High.INTC)
plt.show()

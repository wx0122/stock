from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances


from pprint import pprint
import matplotlib.pyplot as plt

# 1. time series
ts = TimeSeries(key='MJGSPLMJ5QF4UQUY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='WTI',interval='1min', outputsize='full')
#pprint(data.head(2))
print data, meta_data
# print data['1. open']
# data['1. open'].plot()
# plt.title('Intraday Times Series for the WTI stock (1 min)')
# plt.show()


# 2. tech indicator
ti = TechIndicators(key='MJGSPLMJ5QF4UQUY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()

# 3. sector Performance
sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()

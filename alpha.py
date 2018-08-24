from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt

ts = TimeSeries(key='MJGSPLMJ5QF4UQUY', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='WTI',interval='1min', outputsize='full')

#pprint(data.head(2))
print data['1. open']
data['1. open'].plot()
plt.title('Intraday Times Series for the WTI stock (1 min)')
plt.show()

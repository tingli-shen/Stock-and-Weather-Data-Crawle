from alpha_vantage.timeseries import TimeSeries
import pandas as pd
ts = TimeSeries(key='EJ69MPM068NGTJ30', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='UNG',interval='60min', outputsize='full')
data=data.reindex(index=data.index[::-1])

header=list(data)
matrix = [[] for x in range(5)]
time_split = [[] for x in range(4)]
'''
hourly_data=[]
now=datetime.datetime.now()
date=data.index[0][8:10]
transaction_date= now.day if now.day==int(date) else now.day-1
for i in range(len(data.index)):
    if int(data.index[i][14:16])==0 and int(data.index[i][8:10])==transaction_date:
        hourly_data.append(i)
'''

for i in range(len(data.index)):
        time_split[0].append(int(data.index[i][0:4]))
        time_split[1].append(int(data.index[i][5:7]))
        time_split[2].append(int(data.index[i][8:10]))
        time_split[3].append(int(data.index[i][11:13])+0.5)
        for j in range(5):
            matrix[j].append(data.iloc[i][j])
output={}
time=["year","month","day","time"]

for i in range(4):
    output[time[i]]=time_split[i]
for i in range(5):
    output[header[i]]=matrix[i]
df = pd.DataFrame(output)
output["love"]=time_split[0]

writer = pd.ExcelWriter('stock.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='United States Natural Gas Fund',index=0)

    
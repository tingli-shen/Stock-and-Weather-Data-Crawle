import datetime
import pandas as pd
import forecastio
import getpass
api_key = "3f07ab0b08d182dc664ac96dfd7abb99"
location_names=["New York","Boston","DC","Chicago","Saint Louis","Detroit"]
location=[(40.71,-74.00),(42.36,-71.05),(38.90,-77.03),(41.87,-87.62),(38.62,-90.19),(42.33,-83.04)]
writer = pd.ExcelWriter('weather.xlsx', engine='xlsxwriter')
def get_weather(location):
    lat = location[0]
    lng = location[1]
    date = datetime.datetime(2018, 9, 18)
    forecast = forecastio.load_forecast(api_key, lat, lng, time=date, units="us")
    attributes = ["apparentTemperature"]
    times = []
    data = {}
    for attr in attributes:
        data[attr] = []
        start = datetime.datetime(2018, 9, 18)
    for offset in range(1, 100):
        forecast = forecastio.load_forecast(api_key, lat, lng, time=start+datetime.timedelta(offset), units="us")
        h = forecast.hourly()
        d = h.data
        for p in d:
            times.append(p.time)
            for attr in attributes:
                data[attr].append(p.d[attr])
    df = pd.DataFrame(data, index=times)
    return df

def write_file(data,location,writer):
    time_split = [[] for x in range(4)]
    temp=[]
    for i in range(len(data)):
        if data.index[i].day==20 and data.index[i].month==12:
                break 
        if i >=20:
            time_split[0].append(data.index[i].year)
            #day,month=data.index[i].day,data.index[i].month if i%24<20 else time_split[2][i-1],time_split[1][i-1]
            time_split[1].append(data.index[i].month)
            time_split[2].append(data.index[i].day)
            time_split[3].append(data.index[i].hour)
            temp.append(data.iloc[i][0])
            '''
            if data.index[i].day==19 and data.index[i].month==12 and data.index[i].hour==3:
                break
            '''
            
    output={}
    time=["year","month","day","hour"]
    
    for i in range(4):
        output[time[i]]=time_split[i]
    output["temperature"]=temp
    df = pd.DataFrame(output)
    df.to_excel(writer, sheet_name=location,index=0)
for i in range(len(location_names)):
    write_file(get_weather(location[i]),location_names[i],writer)



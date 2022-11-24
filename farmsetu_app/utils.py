from farmsetu_app.models import WeatherData

def get_weather_data():
    data=WeatherData.objects.all()
    data=list(data)
    weather_data=[]
    for row in data:
        value=[row.year, row.jan,
            row.feb, row.mar,
            row.apr, row.may,
            row.jun, row.jul,
            row.aug, row.sep,
            row.oct, row.nov,
            row.dec, row.winter,
            row.spring, row.summer,
            row.autumn, row.annual
        ]
        weather_data.append(value)
    heading=['year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'winter', 'spring', 'summer', 'autumn', 'annual']
    return heading,weather_data
  
        

def insertion_script():
    
    file=open("UK.txt")
    read=file.readlines()[5:]
    for i in range(len(read)):
        read[i]=read[i].split()
    heading=read[0]
    for row in read[1:]:   
        # for i in range(18):
        #     if row[i]=='---':
        #         row[i]=0
        #     else:
        #         row[i]=float(row[i])
        dct={}
        for i in range(len(row)):
            id=heading[i]
            value=0 if not row[i] or row[i]=='---' else float(row[i])
            dct[id]=value
            
        obj=WeatherData(**dct) 
        obj.save() 
    # row=read[1]



    # temp_data=read[1:]
    # return (heading,temp_data)


  

def get_weather_data():
    file=open("UK.txt")
    read=file.readlines()[5:]
    for i in range(len(read)):
        read[i]=read[i].split()
    heading=read[0]
    temp_data=read[1:]
    return (heading,temp_data)


  
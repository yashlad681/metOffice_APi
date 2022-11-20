# metOffice_APi

## API used in this project are as below 


| API | Description |
| ------ | ----------- |
|1.) val/wxfcs/all/datatype/sitelist | From the mentioned resource URL  provided in Met Office documentation we get list of locations with their id's and names.|
|2.) val/wxfcs/all/datatype/locationId | From 1st api the id's we get we pass it to the 2nd api endpoint to get details of weather in that location id. |

### Additional Info

In the views.py file home function has the below condition on line 41

> if count==10:

This counter is set to 10 so it only shows 10 values when the application is run

#### Running and Testing

Endpoint is my localhost, running the below should show desired output.
```
http://127.0.0.1:8000/
```

The code is tested using Postman.


   




import urllib2
import json

url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyC5e31J4CEa1ROwKhXlJevQ6CtmJ0xK_4M"
code = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": 1,
      "infantInLapCount": 0,
      "infantInSeatCount" : 0,
      "childCount" : 0,
      "seniorCount" :0
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "FRA",
        "destination": "BOM",
        "date": "2017-10-09",
      },
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "BOM",
        "destination": "FRA",
        "date": "2017-10-25",
      }

    ],
    "refundable": "false",
    "solutions": 1
  }
}
jsonreq = json.dumps(code, encoding = 'utf-8')
req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})

try:
    flight = urllib2.urlopen(req)

except urllib2.HTTPError, e:
    print( "sss", e.fp.read())
response = flight.read()



response = json.loads(response)
#print response 
i = 0
while(i < len(response["trips"]["tripOption"])):
    print "Option "+str(i+1)
    print ("Sale total: %s " %(response["trips"]["tripOption"][i]["saleTotal"]))
    k=0
    response1 = response["trips"]["tripOption"][i]["slice"]
    #print "response1 = " + str(len(response1))
    while (k < len(response1)):
       # print "segmnet = " + str(len(response1[k]["segment"]))
        j=0
        while (j< len(response1[k]["segment"])):
            for info in (response1[k]["segment"][j]["leg"]):
                print ("Source: %s , Destination: %s , departure time : %s , arrival time : %s "%(
                info["origin"],
                info["destination"],
                info["departureTime"], 
                info["arrivalTime"]))
            j=j+1
        k= k+1
    i= i+1
    
    
    

             
    
'''version 1
for info in (response["trips"]["tripOption"][1]["slice"][0]["segment"][0]["leg"]):
    print ("Source: %s , Destination: %s ,departure time : %s , arrival time : %s "%( info["origin"], info["destination"],info["departureTime"], info["arrivalTime"]))

for info in (response["trips"]["tripOption"][1]["slice"][0]["segment"][1]["leg"]):
    print ("Source: %s , Destination: %s ,departure time : %s , arrival time : %s "%( info["origin"], info["destination"],info["departureTime"], info["arrivalTime"]))
    print ("Sale total: %s " %(response["trips"]["tripOption"][1]["saleTotal"]))
'''

#flight.close()
#print(row)
#print(response)
                                                                                                                                                                           


#from pprint import pprint
import urllib2
import json
#from BeautifulSoup import BeautifulSoup
#from sys import argv

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
        "date": "2016-10-25",
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
#print ("specify targetfile")###
#targetfile = raw_input('>')###
#targetfiletxt = open(targetfile,'w')###
#targetfiletxt.write(response)####
#response = json.loads(flight)
#print(response)

#soup = BeautifulSoup(response)
#output =  [x for x in response if x=['saleTotal'] ]
#print(output)


response = json.loads(response)

for info in (response["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"]):
     print ("Source: %s , Destination: %s ,departure time : %s arrival time : %s "%( info["origin"], info["destination"],info["departureTime"], info["arrivalTime"]))
      

#for info in (response["trips"]["tripOption"][1]["slice"][0]["segment"][0]["leg"]):
 #     print ("Source: %s , Destination: %s ,departure time : %s arrival time : %s "%( info["origin"], info["destination"],info["departureTime"], info["arrivalTime"]))




#flight.close()
#print(row)
#print(response)
                                                                                                                                                                           


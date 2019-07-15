import requests
import pandas
import bs4
from bs4 import BeautifulSoup
#read in postcard Data
//file location
my_data = pandas.read_csv("C://Users//SEAB//Downloads//myPostcardsData.csv")
idList = my_data.itemId.tolist()
//API calls are restricted to 5000 per day. For testing we want to work with less.
idList200 = idList[0:200]

xml = """<?xml version="1.0" encoding="utf-8"?><GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <Version>1085</Version>
  <RequesterCredentials>
    <eBayAuthToken>YourTokenhere</eBayAuthToken>
  </RequesterCredentials>
  <MessageID>XML call: OAuth Token in trading</MessageID>
   <DetailLevel>ItemReturnAttributes</DetailLevel>
  <ItemID>254140401476</ItemID><OutputSelector>Item.PictureDetails.PictureURL</OutputSelector>
  <IncludeItemSpecifics>false</IncludeItemSpecifics>
</GetItemRequest>"""

myRequest = BeautifulSoup(xml)
headers = {'Content-Type': 'text/xml', 'X-EBAY-API-CALL-NAME': 'GetItem',
            'X-EBAY-API-COMPATIBILITY-LEVEL' : '1085',
            'X-EBAY-API-SITEID': '0'}
picLinksFront = [None]*200
picLinksBack = [None]*200
for i in range(len(idList200)):
    myRequest.itemid.string.replace_with(str(idList[i]))
    myText = requests.post('https://api.ebay.com/ws/api.dll', data=xml, headers=headers).text

    myResponse = BeautifulSoup(myText)
    if(myResponse.pictureurl is not None):
        temp = myResponse.findAll('pictureurl')
        tempStrings = [None]*len(temp)
        for j in range(len(temp)):
            tempStrings[j] = temp[j].get_text()
        picLinksFront[i] = tempStrings[0]
        picLinksBack[i] = tempStrings[1]
    else:
        picLinksFront[i] = "invalidItem"
        picLinksBack[i] = "invalidItem"

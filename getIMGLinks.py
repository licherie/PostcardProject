import requests
import pandas
import config
import bs4
from bs4 import BeautifulSoup
#read in postcard Data
#file location
my_data = pandas.read_csv("C://Users//SEAB//Downloads//myPostcardsData.csv")
idList = my_data.itemId.tolist()
#API calls are restricted to 5000 per day. For testing we want to work with less.
idList5 = idList[0:5]

xml = f"""<?xml version="1.0" encoding="utf-8"?><GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <Version>1085</Version>
  <RequesterCredentials>
    <eBayAuthToken>YourTokenhere</eBayAuthToken>
  </RequesterCredentials>
  <MessageID>XML call: OAuth Token in trading</MessageID>
   <DetailLevel>ItemReturnAttributes</DetailLevel>
  <ItemID>{id}</ItemID><OutputSelector>Item.PictureDetails.PictureURL</OutputSelector>
  <IncludeItemSpecifics>false</IncludeItemSpecifics>
</GetItemRequest>"""

myRequest = BeautifulSoup(xml)
myRequest.requestercredentials.ebayauthtoken.string.replace_with(config.AUTH_TOKEN)

headers = {'Content-Type': 'text/xml', 'X-EBAY-API-CALL-NAME': 'GetItem',
            'X-EBAY-API-COMPATIBILITY-LEVEL' : '1085',
            'X-EBAY-API-SITEID': '0'}
picLinksFront = [None]*5
picLinksBack = [None]*5
for i, currentItem in enumerate(idList5):
    xml = f"""<?xml version="1.0" encoding="utf-8"?><GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <Version>1085</Version>
  <RequesterCredentials>
    <eBayAuthToken>{config.AUTH_TOKEN}</eBayAuthToken>
  </RequesterCredentials>
  <MessageID>XML call: OAuth Token in trading</MessageID>
   <DetailLevel>ItemReturnAttributes</DetailLevel>
  <ItemID>{currentItem}</ItemID><OutputSelector>Item.PictureDetails.PictureURL</OutputSelector>
  <IncludeItemSpecifics>false</IncludeItemSpecifics>
</GetItemRequest>"""
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

import requests
xml = """<?xml version="1.0" encoding="utf-8"?><GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <Version>1085</Version>
  <RequesterCredentials>
    <eBayAuthToken>YourTokenHere</eBayAuthToken>
  </RequesterCredentials>
  <MessageID>XML call: OAuth Token in trading</MessageID>
  <DetailLevel>ItemReturnAttributes</DetailLevel>
  <ItemID>254140401476</ItemID><OutputSelector>Item.PictureDetails.PictureURL</OutputSelector>
  <IncludeItemSpecifics>false</IncludeItemSpecifics>
</GetItemRequest>"""
headers = {'Content-Type': 'text/xml', 'X-EBAY-API-CALL-NAME': 'GetItem',
'X-EBAY-API-COMPATIBILITY-LEVEL' : '1085',
'X-EBAY-API-SITEID': '0'}
r = requests.post('https://api.ebay.com/ws/api.dll', data=xml, headers=headers)
myText = requests.post('https://api.ebay.com/ws/api.dll', data=xml, headers=headers).text
print(myText)

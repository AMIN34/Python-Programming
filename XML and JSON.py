#import xml.etree.ElementTree as ET
#data='''
#<person>
#    <name>Amin</name>
#    <phone type='intl'>
#    +918509088268
#    </phone>
#    <email hide='yes' />
#</person>'''
#tree= ET.fromstring(data)
#print('Name:', tree.find('name').text)
#print('Attr:', tree.find('email').get('hide'))

#import xml.etree.ElementTree as ET
#input='''
#<stuff>
#    <users>
#        <user x='2'>
#            <id>007</id>
#            <name>Amin</name>
#        </user>
#        <user x='4'>
#            <id>008</id>
#            <name>Brenner</name>
#        </user>
#    </users>
#</stuff>'''
#stuff=ET.fromstring(input)
#lst1=stuff.findall('users/user')
#print('User Count:', len(lst1))

#lst2=stuff.findall('users')
#print('User Count:',len(lst2))

'''import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter location:')
print('Retrieving', url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
data=data.decode()
tree = ET.fromstring(data)
lines=tree.findall('comments/comment')
count=0
c=0
for i in lines:
    i=int(i.find('count').text)
    count=count+i
    c=c+1
print('Count:', c)
print('Sum:',count)'''

'''import json
import urllib.request, urllib.parse, urllib.error
import ssl
url = input('Enter location: ')
print('Retrieving', url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
data=data.decode()
info = json.loads(data)

count=0
sums=0
for item in info['comments']:
    i=int(item['count'])
    sums=sums+i
    count += 1
print('Count:', count)
print('Sum:', sums)'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address = input('Enter location (please press Enter blank text to exit): ')
    if len(address) < 1: 
        break
    parms = dict()
    parms['address'] = address
    if api_key is not False: 
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    placeid=js['results'][0]['place_id']
    print('Place id', placeid)
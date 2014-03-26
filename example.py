import pyPostcode

postcodeapi = pyPostcode.Api('{YOUR_API_KEY}')

print '\n===', 'using p4 search:'
result = postcodeapi.getaddress('5041')
print ":", result._data if result else 'None'

print '\n===', 'using p5 search:'
result = postcodeapi.getaddress('5041E')
print ":", result._data if result else 'None'

print '\n===', 'using p6 search:'
result = postcodeapi.getaddress('5041EB')
print ":", result._data if result else 'None'

print '\n===', 'using address search (p6 + house number):'
result = postcodeapi.getaddress('5041EB', 21) # use address search
print ":", result._data if result else 'None'

import pyPostcode

postcodeapi = pyPostcode.Api('{YOUR_API_KEY}')

print '\n===', 'using p4 search:'
result = postcodeapi.getaddress('4321')
print ":", result._data if result else 'None'
if result:
    print 'https://www.google.nl/maps/@{0},{1},14z'.format(
        result.latitude, result.longitude)

print '\n===', 'using p5 search:'
result = postcodeapi.getaddress('4321A')
print ":", result._data if result else 'None'
if result:
    print 'https://www.google.nl/maps/@{0},{1},16z'.format(
      result.latitude, result.longitude)

print '\n===', 'using p6 search:'
result = postcodeapi.getaddress('4321 AB')
print ":", result._data if result else 'None'
if result:
    print 'https://www.google.nl/maps/@{0},{1},18z'.format(
        result.latitude, result.longitude)

print '\n===', 'using address search (p6 + house number):'
result = postcodeapi.getaddress('4321 AB', 5)
print ":", result._data if result else 'None'
if result:
    print 'https://www.google.nl/maps/@{0},{1},20z'.format(
        result.latitude, result.longitude)

print '\n===', 'using address search (p6 + house number) with BAG details:'
result = postcodeapi.getaddress('4321 AB', 5, True)
print ":", result._data if result else 'None'
if result:
    print 'https://www.google.nl/maps/@{0},{1},20z'.format(
        result.latitude, result.longitude)

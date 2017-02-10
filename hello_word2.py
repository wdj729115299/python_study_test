shoplist = ['apple', 'orange', 'banana', 'carrot']

print 'I have ', len(shoplist), ' items to purchase.'

print 'these items are:'
for item in shoplist:
    print item,

print 'I alse have to buy rice'
shoplist.append('rice')

print 'these items are:'
for item in shoplist:
    print item,

print 'I will sort my list'
shoplist.sort()
print 'these items are:'
for item in shoplist:
    print item,

print '\n'
print 'fist item is'
print shoplist[0]
del shoplist[0]

print 'first item is'
print shoplist[0]


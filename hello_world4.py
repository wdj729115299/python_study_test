ab = { 'yanghuan' : '123@qq.com',
       'lvlu' : '123@www.com',
       'yangyan' : 'dfd@dfd.com',
       'xiahuijun' : '345@234.com',
     }

print 'lvlu email address is %s' % ab['lvlu']

ab['zhengsuxian'] = 'hello@dfld.org'

del ab['yanghuan']

print '%d' % len(ab)

for name, address in ab.items():
    print '%s %s' % (name, address)

if 'yangyan' in ab:
    print '%s', ab['yangyan']
names = {'k1':'v1', 'k2':'v2'}
attrs = {}
cls = type('MyClass', (object,), {})
for key in names:
    print(names[key])
    #attrs[key] = names[key]
    #attrs[key] = lambda key: names[key]
    attrs[key] = property(lambda cls: names[key])
print(key)
print(attrs)
#for key in attrs:
#    print(attrs[key](key))
for key in attrs:
    setattr(cls, key, names[key])
#    setattr(cls, key[0].upper()+key[1].lower(), names[key])
    
    setattr(cls, key[0].upper()+key[1].lower(), property(lambda cls: cls.__getattribute__(key)))
    #setattr(cls, key[0].upper()+key[1].lower(), property(lambda cls: print(dir(cls))))
    #setattr(cls, key[0].upper()+key[1].lower(), property(lambda cls: getattr(cls, f'_{cls.__name__}__{key}')))
#    setattr(cls, key[0].upper()+key[1].lower(), property(lambda cls: names[key]))
#    setattr(cls, key[0].upper()+key[1].lower(), property(lambda cls: getattr(cls, key)))
    #setattr(cls, key, property(lambda cls: getattr(cls, names[key])))
    #setattr(cls, key, property(lambda cls: names[key]))
    #setattr(cls, key, attrs[key])
    #print(getattr(cls, key))
    #print(getattr(cls(), key[0].upper()+key[1].lower()))

"""
for key in attrs:
    #print(type(key), key, id(key))
    print(getattr(cls, key))
    print(getattr(cls(), key[0].upper()+key[1].lower()))
print(cls().k1)
print(cls().k2)
c = cls()
print(c.k1)
print(c.k2)

print(getattr(cls(), 'k1'))
print(getattr(cls(), 'k2'))
"""
print(getattr(cls(), 'K1'))
print(getattr(cls(), 'K2'))
#c = cls()
#c.K2 = 'abc'
#print(c.K2)

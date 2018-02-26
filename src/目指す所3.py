#!python3
#encoding:utf-8
#http://y0m0r.hateblo.jp/entry/20120116/1326715412
import inspect
class Db: pass
    #def __GetSection1Key1(self): return self.__Section1Key1
#    def __Get{propName}(self): return self.__{propName}
#    {propName} = property(__Get{propName})

if __name__ == '__main__':
    ATTRS = (('Section1','Key1','Value1'),('Section1','Key2','Value2'))
    for attr in ATTRS:
        setattr(Db, '_{}__{}{}'.format(Db.__name__, attr[0], attr[1]), attr[2])
        def Getter(self):
            methodName = inspect.currentframe().f_code.co_name
            propName = methodName.replace('Get','')
            varName = '_{}__{}'.format(Db.__name__, propName)
            return getattr(self, varName)
        setattr(Db, 'Get{}{}'.format(attr[0], attr[1]), Getter)
    print(dir(Db))
    assert(hasattr(Db, 'GetSection1Key1'))
    assert(hasattr(Db, 'GetSection1Key2'))
    db = Db()
    print(db.GetSection1Key1())
    print(db.GetSection1Key2())
"""
# Value2になる
class Db: pass
if __name__ == '__main__':
    ATTRS = (('Section1','Key1','Value1'),('Section1','Key2','Value2'))
    for attr in ATTRS:
        def Getter(self): return attr[2]
        setattr(Db, 'Get{}{}'.format(attr[0], attr[1]), Getter)
    print(dir(Db))
    assert(hasattr(Db, 'GetSection1Key1'))
    assert(hasattr(Db, 'GetSection1Key2'))
    db = Db()
    print(db.GetSection1Key1())
    print(db.GetSection1Key2())
"""

#http://y0m0r.hateblo.jp/entry/20120116/1326715412
class Db: pass
if __name__ == '__main__':
    db = Db()
    ATTRS = (('Section1','Key1','Value1'),('Section1','Key2','Value2'))
    for attr in ATTRS:
        def Getter(self): return attr[2]
        setattr(db, 'Get{}{}'.format(attr[0], attr[1]), Getter)
        setattr(db, '{}{}'.format(attr[0], attr[1]), property(lambda db: getattr(db, 'Get{}{}'.format(attr[0], attr[1]))))
    print(dir(db))
    assert(hasattr(db, 'GetSection1Key1'))
    assert(hasattr(db, 'GetSection1Key2'))
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))
    print(db.GetSection1Key1())
    print(db.GetSection1Key2())
    print(db.Section1Key1)
    print(db.Section1Key2)

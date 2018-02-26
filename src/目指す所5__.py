class Db:
    ATTRS = (('Section1','Key1','Value1'),('Section1','Key2','Value2'))
    def __init__(self):
        self.__Section1Key1 = 'Value1'
        self.__Section1Key2 = 'Value2'
        for attr in Db.ATTRS:
            propName = Db.ATTRS[0] + Db.ATTRS[1]
            Db[] = property(getattr(Db, f'__Get{0}'))
    def __GetSection1Key1(self): return self.__Section1Key1
    Section1Key1 = property(getattr(Db, f'__Get{0}'))
    def __GetSection1Key2(self): return self.__Section1Key2
    Section1Key2 = property(__GetSection1Key2)


if __name__ == '__main__':
    db = Db()
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))

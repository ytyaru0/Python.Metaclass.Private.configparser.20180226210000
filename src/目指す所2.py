class Db:
    def __init__(self):
        self.__Section1Key1 = 'Value1'
        self.__Section1Key2 = 'Value2'
    def __GetSection1Key1(self): return self.__Section1Key1
    Section1Key1 = property(__GetSection1Key1)
    def __GetSection1Key2(self): return self.__Section1Key2
    Section1Key2 = property(__GetSection1Key2)


if __name__ == '__main__':
    db = Db()
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))
    print(db.Section1Key1)
    print(db.Section1Key2)

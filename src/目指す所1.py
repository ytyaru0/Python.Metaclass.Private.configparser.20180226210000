class Db:
    def __init__(self):
        self.__Section1Key1 = 'Value1'
        self.__Section1Key2 = 'Value2'
    @property
    def Section1Key1(self): return self.__Section1Key1
    @property
    def Section1Key2(self): return self.__Section1Key2


if __name__ == '__main__':
    db = Db()
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))
    print(db.Section1Key1)
    print(db.Section1Key2)

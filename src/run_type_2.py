if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # attributes生成
    attrs = {}
    varName1 = '_{}__{}{}'.format(name, 'Section1', 'Key1')
    attrs[varName1] = 'Value1'
    varName2 = '_{}__{}{}'.format(name, 'Section1', 'Key2')
    attrs[varName2] = 'Value2'
    print(attrs)

    # class生成
    cls = type(name, (object,), attrs)
    print(cls.__name__)
    print(dir(cls))
    print(cls._Db__Section1Key1)
    #   property生成
    propName1 = '{}{}'.format('Section1', 'Key1')
    propName2 = '{}{}'.format('Section1', 'Key2')
    setattr(cls, propName1, property(lambda cls: getattr(cls, varName1)))
    setattr(cls, propName2, property(lambda cls: getattr(cls, varName2)))

    print(hasattr(cls, varName1))
    print(hasattr(cls, propName1.format('Section1', 'Key1')))
    print(hasattr(cls, propName1.format('Section1', 'Key2')))
    print(cls._Db__Section1Key1)
    print(cls._Db__Section1Key2)
    print(cls.Section1Key1)
    print(cls.Section1Key2)
    c = cls()
    print(c)
    print(c.Section1Key1)
    print(c.Section1Key2)
    #print(cls().Section1Key1)
    #print(cls().Section1Key1)

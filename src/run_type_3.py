if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # attributes生成
    attrs = {}
    Keys = {'Key1':'Value1', 'Key2':'Value2'}
    for key, val in Keys.items():
        varName = '_{}__{}{}'.format(name, 'Section1', key)
        attrs[varName] = Keys[key]
    print(attrs)

    # class生成
    cls = type(name, (object,), attrs)
    print(cls.__name__)
    print(dir(cls))
    print(cls._Db__Section1Key1)
    #   property生成
    for key, val in Keys.items():
        propName = '{}{}'.format('Section1', key)
        varName = '_{}__{}{}'.format(name, 'Section1', key)
        setattr(cls, propName, property(lambda cls: getattr(cls, varName)))

    # 確認
    for key, val in Keys.items():
        varName = '_{}__{}{}'.format(name, 'Section1', key)
        print(hasattr(cls, varName))
        propName = '{}{}'.format('Section1', key)
        print(hasattr(cls, propName))
        print(getattr(cls(), propName))
    print(cls().Section1Key1)
    print(cls().Section1Key2)

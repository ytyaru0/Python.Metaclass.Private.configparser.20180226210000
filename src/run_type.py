if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # attributes生成
    attrs = {}
    attrs['_{}__{}{}'.format(name, 'Section1', 'Key1')] = 'Value1'
    attrs['_{}__{}{}'.format(name, 'Section1', 'Key2')] = 'Value2'
    print(attrs)

    # class生成
    cls = type(name, (object,), attrs)
    print(cls.__name__)
    print(dir(cls))
    print(cls._Db__Section1Key1)
    #   property生成
    setattr(cls, '{}{}'.format('Section1', 'Key1'), property(lambda cls: getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key1'))))
    setattr(cls, '{}{}'.format('Section1', 'Key2'), property(lambda cls: getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key2'))))
    #setattr(cls, '{}{}'.format('Section1', 'Key1'), property(lambda cls: getattr(cls, attrs['_{}__{}{}'.format(name, 'Section1', 'Key1')])))
    #setattr(cls, '{}{}'.format('Section1', 'Key1'), property(lambda cls: getattr(cls, attrs['_{}__{}{}'.format(cls.__name__, 'Section1', 'Key1')])))

    print(hasattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key1')))
    print(hasattr(cls, '{}{}'.format('Section1', 'Key1')))
    print(hasattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key2')))
    print(hasattr(cls, '{}{}'.format('Section1', 'Key2')))
    print(cls._Db__Section1Key1)
    print(cls._Db__Section1Key2)
    print(cls.Section1Key1)
    print(cls.Section1Key2)
    print(cls().Section1Key1)
    print(cls().Section1Key2)

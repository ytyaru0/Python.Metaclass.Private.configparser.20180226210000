if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # Attributes生成
    attrs = {}
    config = configparser.ConfigParser()
    config.read('config.ini')
    for section in config:
        for key in config[section]: # キー名は小文字になってしまうので注意！
            attrs['_{}__{}{}'.format(name, section, key)] = config[section][key]
    print(attrs)

    # Class生成
    cls = type(name, (object,), attrs)
    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key1')))
    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key2')))

    #   property生成
    #getters = {}
    #for section in config:
    #    for key in config[section]: # キー名は小文字になってしまうので注意！
    #        getters['{}{}'.format(section, key)] = lambda cls: getattr(cls, '_{}__{}{}'.format(name, section, key))

    print(cls.__name__)
    print(dir(cls))
    for section in config:
        for key in config[section]: # キー名は小文字になってしまうので注意！
            setattr(cls, '{}{}'.format(section, key), property(lambda cls: getattr(cls, '_{}__{}{}'.format(name, section, key))))
            #getter = lambda cls: getattr(cls, '_{}__{}{}'.format(name, section, key))
            #setattr(cls, '{}{}'.format(section, key), property(getter))
            #setattr(cls, '{}{}'.format(section, key), property(getters['{}{}'.format(section, key)]))
    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key1')))
    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key2')))
    print('#', getattr(cls(), '{}{}'.format('Section1', 'key1')))
    print('#', getattr(cls(), '{}{}'.format('Section1', 'key2'))) # Value2になるべきなのにValue1になってしまう

    """
    # 確認
    for section in config:
        for key in config[section]:
            print(hasattr(cls, '_{}__{}{}'.format(name, section, key)), name, section, key)
            print(hasattr(cls, '{}{}'.format(section, key)))

    
    print(hasattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key1')))
    print(hasattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key2')))
    print(hasattr(cls, '{}{}'.format('Section1', 'key1')))
    print(hasattr(cls, '{}{}'.format('Section1', 'key2')))

    print(getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key1')))
    print(getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'key2')))
    print(getattr(cls(), '{}{}'.format('Section1', 'key1')))
    print(getattr(cls(), '{}{}'.format('Section1', 'key2')))

    print(cls._Db__Section1key1)
    print(cls._Db__Section1key2)
    print(cls().Section1key1) # ※Value2になってる謎！
    print(cls().Section1key2)
    """
    """
    #変数に再代入するとFalseになる。for文で回しているときの値はstr型でないのか？でもstr.format()で文字列のはず。謎
    #section = 'Section1'
    #key = 'Key1'
    print(hasattr(cls, '_{}__{}{}'.format(name, section, key)), name, section, key)
    print(hasattr(cls, '{}{}'.format(section, key)))
    #print(cls._Db__Section1Key1)
    #print(cls.Section1Key1)
    """

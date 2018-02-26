if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # Attributes生成
    attrs = {}
    config = configparser.ConfigParser()
    config.read('config.ini')
    for section in config:
        for key in config[section]:
            attrs['_{}__{}{}'.format(name, section, key)] = config[section][key]
    print(attrs)

    # Class生成
    cls = type(name, (object,), attrs)
    print(cls.__name__)
    print(dir(cls))
    for section in config:
        for key in config[section]:
            print(section, key, config[section][key])
            section = str(section)
            key = str(key)
            setattr(cls, '{}{}'.format(section, key), property(lambda cls: getattr(cls, '_{}__{}{}'.format(name, section, key))))
            #なぜかfor文内でのみTrueになる！
            #print(hasattr(cls, '_{}__{}{}'.format(name, section, key)), name, section, key)
            #print(hasattr(cls, '{}{}'.format(section, key)))


    #変数に再代入するとFalseになる。for文で回しているときの値はstr型でないのか？でもstr.format()で文字列のはず。謎
    section = 'Section1'
    key = 'key1' # 原因はこれ。なぜか`for key in config[section]:`のkeyは小文字になる
    #key = 'Key1'
    print(hasattr(cls, '_{}__{}{}'.format(name, section, key)), name, section, key)
    print(hasattr(cls, '{}{}'.format(section, key)))
    print(cls._Db__Section1key1)
    print(cls._Db__Section1key2)
    print(cls.Section1key1)
    print(cls.Section1key2)
    print(cls().Section1key1)
    print(cls().Section1key2)

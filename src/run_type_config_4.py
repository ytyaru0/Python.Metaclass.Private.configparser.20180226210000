if __name__ == '__main__':
    import configparser
    # Class名
    name = 'Db'

    # 名前生成
    config = configparser.ConfigParser()
    config.read('config.ini')
    attrNames = {}
    for section in config:
        for key in config[section]: # キー名は小文字になってしまうので注意！
            s = section[0].upper() + section[1:].lower()
            k = key[0].upper() + key[1:].lower()
            propName = '{}{}'.format(s, k)
            varName = '_{}__{}{}'.format(name, s, k)
            attrNames[propName] = [varName, config[section][key]]

    # クラスオブジェクト生成
    cls = type(name, (object,), {})

    # getter作成
    for propName in attrNames.keys():
        attrNames[propName].append(lambda cls: getattr(cls, attrNames[propName][0]))

    print(attrNames)

    # Attributes生成
    cls = type(name, (object,), {})
    for propName in attrNames.keys():
        setattr(cls, attrNames[propName][0], attrNames[propName][1])
        setattr(cls, propName, property(attrNames[propName][2]))
        #setattr(cls, propName, property(lambda cls: getattr(cls, attrNames[propName][0])))

    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key1')))
    print('*', getattr(cls, '_{}__{}{}'.format(name, 'Section1', 'Key2')))
    print('#', getattr(cls(), '{}{}'.format('Section1', 'Key1')))
    print('#', getattr(cls(), '{}{}'.format('Section1', 'Key2'))) # Value2になるべきなのにValue1になってしまう


import configparser
class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        cls.__SetAttributes(cls, name)

    @classmethod
    def __SetAttributes(cls, target, name):
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')
        for section in cls.config:
            for key in cls.config[section]:
                # 2通りの方法どちらもなぜかValue1！
                # print(target().Section1Key2) # ※なぜかValue1！
                print(section, key, cls.config[section][key])
                varName = cls.__GetVarName(name, section, key)
                propName = cls.__GetPropName(section, key)
                setattr(target, varName, cls.config[section][key]) # Db.Secretプロパティ定義
                setattr(target, propName, property(lambda target: getattr(target, varName)))
                """
                s = section[0].upper() + section[1:].lower()
                k = key[0].upper() + key[1:].lower()# ※※※keyはすべて小文字になってしまうので！※※※
                varName = '_{}__{}{}'.format(name, s, k)
                propName = '{}{}'.format(s, k)
                setattr(target, varName, cls.config[section][key]) # Db.Secretプロパティ定義
                setattr(target, propName, property(lambda target: getattr(target, varName)))
                """

                print(varName)
                print(propName)
                print(hasattr(target, varName))
                print(hasattr(target, propName))

        section = 'Section1'
        key = 'Key1'
        print(hasattr(target, '_{}__{}{}'.format(name, section, key)), name, section, key)
        print(hasattr(target, '{}{}'.format(section, key)))
        varName = '_{}__{}{}'.format(name, section, key)
        print(varName, getattr(target, varName))
        propName = '{}{}'.format(section, key)
        print(varName, getattr(target, propName), getattr(target(), propName))
        print(target._Db__Section1Key1)
        print(target().Section1Key1)
        print(target._Db__Section1Key2)
        print(target().Section1Key2) # ※なぜかValue1！

    @classmethod
    def __GetVarName(cls, name, section, key): return '_{0}__{1}'.format(name, cls.__GetPropName(section, key))
    @classmethod
    def __GetPropName(cls, section, key):
        return cls.__FirstUpperCamelcase(section) + cls.__FirstUpperCamelcase(key)
    @classmethod
    def __FirstUpperCamelcase(cls, word):
        return word[0].upper() + word[1:].lower()


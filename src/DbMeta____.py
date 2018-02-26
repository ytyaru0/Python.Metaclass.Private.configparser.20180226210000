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
                print(section, key, cls.config[section][key])
                s = section[0].upper() + section[1:].lower()
                k = key[0].upper() + key[1:].lower()# ※※※keyはすべて小文字になってしまうので！※※※
                varName = '_{}__{}{}'.format(name, s, k)
                propName = '{}{}'.format(s, k)
                setattr(target, varName, cls.config[section][key]) # Db.Secretプロパティ定義
                setattr(target, propName, property(lambda target: getattr(target, varName)))
                print(varName)
                print(propName)
                print(hasattr(target, varName), name, s, k)
                print(hasattr(target, propName))

        section = 'Section1'
        key = 'Key1'
        print(hasattr(target, '_{}__{}{}'.format(name, section, key)), name, section, key)
        print(hasattr(target, '{}{}'.format(section, key)))
        varName = '_{}__{}{}'.format(name, section, key)
        print(varName, getattr(target, varName))
        propName = '{}{}'.format(section, key)
        print(varName, getattr(target, propName), getattr(target(), propName))
            
        """
        for key, val in cls.__makeVars.items():
            setattr(target, '_{0}__{1}'.format(name, key), val) # Db.Secretプロパティ定義
            setattr(target, key, property(lambda target: getattr(target, '_{0}__{1}'.format(name, key)))) # Db.Secretプロパティ定義
        """
        """
            #注意！以下のようにするとプロパティ返却値がすべて同一になってしまう！なぜ？
            varname = '_{0}__{1}'.format(name, key)
            setattr(target, varname, val) # Db.Secretプロパティ定義
            setattr(target, key, property(lambda target: getattr(target, varname))) # Db.Secretプロパティ定義
        """
        """
        for key, val in cls.__makeVars.items():
            print(key, getattr(target, key), getattr(target(), key))
        """


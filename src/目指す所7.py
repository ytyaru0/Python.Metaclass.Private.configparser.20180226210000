#http://y0m0r.hateblo.jp/entry/20120116/1326715412
#class Db: pass
class CodeTemplate:
    def __init__(self, ClassName):
        self.__cls = f'class {ClassName}:\n'
        self.__init = '    def __init__(self):\n'
        self.__setAttr = "        self.__{PropertyName} = '{Value}'\n"
        self.__decorator = '    @property\n'
        self.__method = '    def {PropertyName}(self): return self.__{PropertyName}\n'
    def Get(self, NameAndValues):
        code = self.__cls + self.__init
        for p, v in NameAndValues.items():
            code += self.__setAttr.format(PropertyName=p, Value=v)
        code += '\n'
        for p in NameAndValues.keys():
            code += self.__decorator
            code += self.__method.format(PropertyName=p) + '\n'
        return code

if __name__ == '__main__':
    # クラスのデータ
    clsName = 'Config'
    propVals = {'Section1Key1':'Value1', 'Section1Key2':'Value2'}
    # クラスのコード生成
    code = CodeTemplate(clsName).Get(propVals)
    print(code)
    # クラスのコード実行
    exec(code)
    # クラス生成
    config = Config()
    print(dir(config))
    # 確認
    assert(hasattr(config, '_Config__Section1Key1'))
    assert(hasattr(config, '_Config__Section1Key2'))
    assert(hasattr(config, 'Section1Key1'))
    assert(hasattr(config, 'Section1Key2'))
    assert(config._Config__Section1Key1 == 'Value1')
    assert(config._Config__Section1Key2 == 'Value2')
    assert(config.Section1Key1 == 'Value1')
    assert(config.Section1Key2 == 'Value2')
    print(config._Config__Section1Key1)
    print(config._Config__Section1Key2)
    print(config.Section1Key1)
    print(config.Section1Key2)

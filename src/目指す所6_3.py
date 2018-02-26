#http://y0m0r.hateblo.jp/entry/20120116/1326715412
#class Db: pass
if __name__ == '__main__':
    # コードのテンプレ
    code_cls = "class {clsName}:\n"
    code_init = "    def __init__(self):\n"
    code_attr = "        self.__{propName} = '{value}'\n"
    code_deco = "    @property\n"
    code_prop = "    def {propName}(self): return self.__{propName}\n"
    # コード生成
    code = code_cls.format(clsName='Db') + code_init
    props = {'Section1Key1':'Value1', 'Section1Key2':'Value2'}
    for prop, value in props.items():
        code += code_attr.format(propName=prop, value=value)
    code += '\n'
    for prop, value in props.items():
        code += code_deco + code_prop.format(propName=prop) + '\n'
    print(code)

    # コード実行
    exec(code)
    
    # コードのクラス生成
    db = Db()
    print(dir(db))



    # 確認
    assert(hasattr(db, '_Db__Section1Key1'))
    assert(hasattr(db, '_Db__Section1Key2'))
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))
    assert(db._Db__Section1Key1 == 'Value1')
    assert(db._Db__Section1Key2 == 'Value2')
    assert(db.Section1Key1 == 'Value1')
    assert(db.Section1Key2 == 'Value2')
    print(db._Db__Section1Key1)
    print(db._Db__Section1Key2)
    print(db.Section1Key1)
    print(db.Section1Key2)

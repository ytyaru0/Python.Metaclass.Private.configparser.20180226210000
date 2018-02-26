#http://y0m0r.hateblo.jp/entry/20120116/1326715412
#class Db: pass
if __name__ == '__main__':
    # コードのテンプレ
    code_cls = "class {clsName}:\n    def __init__(self):\n"
    code_init = "        self.__{propName} = '{value}'\n"
    code_prop = "    @property\n    def {propName}(self): return self.__{propName}\n"
    # コード生成
    code = code_cls.format(clsName='Db')
    props = {'Section1Key1':'Value1', 'Section1Key2':'Value2'}
    for prop, value in props.items():
        code += code_init.format(propName=prop, value=value)
    for prop, value in props.items():
        code += code_prop.format(propName=prop)
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

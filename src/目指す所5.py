#http://y0m0r.hateblo.jp/entry/20120116/1326715412
#class Db: pass
if __name__ == '__main__':
    code_cls = """
class {clsName}:
    def __init__(self):
"""
    code_init = """        self.__{propName} = '{value}'
"""
    code_prop = """
    def __Get{propName}(self): return self.__{propName}
    {propName} = property(__Get{propName})
"""

    code = code_cls.format(clsName='Db')
    props = {'Section1Key1':'Value1', 'Section1Key2':'Value2'}
    for prop, value in props.items():
        code += code_init.format(propName=prop, value=value)
    for prop, value in props.items():
        code += code_prop.format(propName=prop)
    print(code)

    exec(code)
    
    db = Db()
    print(dir(db))
    """
    assert(hasattr(db, 'GetSection1Key1'))
    assert(hasattr(db, 'GetSection1Key2'))
    assert(hasattr(db, 'Section1Key1'))
    assert(hasattr(db, 'Section1Key2'))
    print(db.GetSection1Key1())
    print(db.GetSection1Key2())
    print(db.Section1Key1)
    print(db.Section1Key2)
    """

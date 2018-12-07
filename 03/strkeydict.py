class StrKeyDict0(dict):

    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self,key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([(2, 'two'), ('4', 'four')])
print(d.get(3))

from  collections import OrderedDict
ord_d = OrderedDict()
ord_d['name']='Daven'
ord_d['age'] = 22
ord_d['height'] = 168
print(ord_d.popitem(last=False))
print(ord_d)
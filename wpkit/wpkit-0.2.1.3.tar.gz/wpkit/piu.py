import json,os,shutil
from collections import deque
from wpkit.basic import T,PointDict,PowerDirPath

def json_load(f,encoding='utf-8',*args,**kwargs):
    import json
    with open(f,'r',encoding=encoding) as fp:
        return json.load(fp,*args,**kwargs)
def json_dump(obj,fp,encoding='utf-8',*args,**kwargs):
    import json
    with open(fp,'w',encoding=encoding) as f:
        json.dump(obj,f,*args,**kwargs)
class Piu:
    def __init__(self,path='./db'):
        self.dbpath=path
        self.dicpath=os.path.join(self.dbpath,'data.dic')
        self.dic=self.setup()
    def setup(self):
        if self._exists():return json_load(self.dicpath)
        return self._make()
    def add(self,key=None,value=None,**kwargs):
        assert (key is None )or isinstance(key,str)
        if key:
            self.dic[key]=value
        self.dic.update(**kwargs)
        self._save()
    def delete(self,key):
        del self.dic[key]
        self._save()
    def get(self,*args,**kwargs):
        return self.dic.get(*args,**kwargs)
    def _save(self):
        json_dump(self.dic,self.dicpath)
    def _exists(self):
        if os.path.exists(self.dbpath) and os.path.exists(self.dicpath):
            return True
        return False
    def _make(self):
        dir=self.dbpath
        shutil.rmtree(dir) if os.path.exists(dir) else None
        os.makedirs(dir)
        dic={}
        json_dump(dic,self.dicpath)
        return dic
class FileDict(PointDict):
    def __init__(self,path):
        self.seta(path=path)
        path = PowerDirPath(self.geta('path'))
        if path.exists():
            assert path.isfile()
            dic=json_load(path)
            assert isinstance(dic,dict)
        else:
            dic={}
            path.tofile()
            json_dump(dic,path,indent=4)
        super().__init__(dic)
    def __setattr__(self, key, value):
        PointDict.__setattr__(self,key,value)
        self._save()
    def __setitem__(self, key, value):
        PointDict.__setitem__(self,key,value)
        self._save()
    def update(self,**kwargs):
        for k,v in kwargs.items():
            self[k]=v
    def _save(self):
        json_dump(self,self.geta('path'),indent=4)




class BackupDB(PointDict):
    def __init__(self, path='./db',ignore_duplicated=True,max_depth=10):
        self.dbpath = path
        self.dicpath = os.path.join(self.dbpath, 'data.json')
        self.configfile=os.path.join(self.dbpath,'config.json')
        self.dic = self.setup()
        self.config=self.setup_configfile()
        self.config.update(ignore_duplicated=ignore_duplicated,max_depth=max_depth)
        self.load_config()
        # self.ignore_duplicated=ignore_duplicated
        # self.max_depth=max_depth
    def setup_configfile(self):
        config=FileDict(self.configfile)
        return config
    def load_config(self):
        for k,v in self.config.items():
            self[k]=v
    def setup(self):
        if self._exists(): return json_load(self.dicpath)
        return self._make()

    def add(self, key=None, value=None, **kwargs):
        assert (key is None) or isinstance(key, str)
        kwargs.update(key=value)
        for k,v in kwargs.items():
            if k not in self.dic.keys():
                self.dic[k] = [v]
            elif self.ignore_duplicated and v==self.dic[k][-1]:
                continue
            else:
                self.dic[k].append(v)
                if len(self.dic[k])>self.max_depth:
                    self.dic[k]=self.dic[k][1:]
        self._save()

    def delete(self, key):
        del self.dic[key]
        self._save()

    def get(self,k, default=T.NOT_GIVEN):
        if k not in self.dic.keys():
            if default==T.NOT_GIVEN:
                raise KeyError('No such key named %s'%(k))
            else:
                return default
        return self.dic[k][-1]

    def recover(self,key,step=1):
        assert key in self.dic.keys()
        assert len(self.dic[key])>step
        return self.dic[key].pop()
    def _save(self):
        json_dump(self.dic, self.dicpath,indent=4)

    def _exists(self):
        if os.path.exists(self.dbpath) and os.path.exists(self.dicpath):
            return True
        return False

    def _make(self):
        dir = self.dbpath
        shutil.rmtree(dir) if os.path.exists(dir) else None
        os.makedirs(dir)
        dic = {}
        json_dump(dic, self.dicpath,indent=4)
        return dic

def demo():
    P = Piu()
    P.add('a', 13)
    P.add('name', 'wangpei')
    P.add('age', 21)
    P.delete('a')
    age = P.get('age')
    print(age)
    x = P.get('x', 30)
    print(x)
if __name__ == '__main__':
    demo()


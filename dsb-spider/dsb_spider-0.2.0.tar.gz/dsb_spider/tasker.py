from dsb_spider.log import getLogger
from dsb_spider.log.ex import DsbException
logger = getLogger('dsb')
from dsb_spider.utils import hash_args

_TASK_FUNC_REGISTERS = {}

class _FuncRegistry():
    def __init__(self, name:str):
        self.name = name
        self.funcs = {}
        
    def update(self, funcs_iter):
        if hasattr(funcs_iter, 'items'):
            funcs_iter = funcs_iter.items()
        for key, value in funcs_iter:
            self[key] = value
            
    def __setitem__(self, key, value):
        if not callable(value):
            raise DsbException(f'func {key} register failed')
        if not key:
            raise ValueError('func name must not be none')
        self.funcs[key] = value
        
    def __getitem__(self, item):
        return self.funcs[item]
    
    def __delitem__(self, key):
        del self.funcs[key]
        
    def __iter__(self):
        return iter(self.funcs)
    
    def items(self):
        return list(self.funcs.items())
    
    def iteritems(self):
        return iter(self.funcs.items())
    
    def clear(self):
        self.funcs.clear()
        
    def __call__(self, obj):
        self[obj.__name__] = obj
        return obj
    
    def __deco(self, name, obj):
        self[name] = obj
        return obj
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return
    
    def __repr__(self):
        return f'<{self.__class__.__name__}|{self.name}>'
    
    def __str__(self):
        return f'<{self.__class__.__name__}|{self.name}>'

def getTaskFuncRegister(name: str):
    try:
        return _TASK_FUNC_REGISTERS[name]
    except KeyError:
        register = _TASK_FUNC_REGISTERS[name] = _FuncRegistry(name)
        return register

# 使用单例保证相同任务运行的唯一性
class TaskSingleton(type):
    _instances = {}
    
    def __call__(cls,*args, **kwargs):
        key = hash_args(*args, **kwargs)
        try:
            instance = cls._instances[key]
        except KeyError:
            instance = cls._instances[key] = super().__call__(*args, **kwargs)
            instance.hash_key = key
        return instance
    
    @classmethod
    def clear(cls, key):
        try:
            del cls._instances[key]
        except KeyError:
            pass

# 定义任务状态: stoped -> ready -> stoped , 只有ready状态可run
# ready:

class StopedState():
    @staticmethod
    def ready(task):
        task.do_ready()
        task.new_state(ReadyState)
    
    @staticmethod
    def run(task):
        raise RuntimeError('Not ready')
    
    @staticmethod
    def stop(task):
        raise RuntimeError('Already stoped')

class ReadyState():
    @staticmethod
    def ready(task):
        raise RuntimeError('Already ready')

    @staticmethod
    def run(task):
        task.do_task()

    @staticmethod
    def stop(task):
        task.do_stop()
        task.new_state(StopedState)
    
# 定义任务阶段： ready -> run -> finish

class Task(object, metaclass=TaskSingleton):
    def __init__(self,name, listener=None, **kwargs):
        self.task_name = name
        self.listenter=listener
        self.register_task_funcs()
        self.new_state(StopedState)
        if hasattr(self, 'init_infos'):
            self.init_infos(**kwargs)
        
    def register_task_funcs(self):
        registry = _TASK_FUNC_REGISTERS[self.task_name]
        for key, value in registry.items():
            setattr(self, key, value)
    
    def new_state(self, state):
        self._state = state
    
    def ready(self):
        self._state.ready(self)
    
    def run(self):
        self._state.run(self)
    
    def finish(self):
        if hasattr(self, 'hash_key'):
            TaskSingleton.clear(self.hash_key)
        self._state.stop(self)
    
if __name__ == '__main__':
    haha = getTaskFuncRegister('haha')
    @haha
    def do_task():
        print('go')

    task = Task('haha')
    task.ready()
    task.run()
    task.finish()



from dsb_spider import log
logger = log.getLogger('dsb')

TaskId = str
Operation = str
Url = str

# 用来去重
class TaskSingleton(type):
    _instances = {}
    
    def __call__(cls,operation: Operation,url: Url, *args, **kwargs):
        if url not in cls._instances:
            cls._instances[url] = super().__call__(*args, **kwargs)
        return cls._instances[url]
    
    @classmethod
    def clear(cls, url: Url):
        try:
            del cls._instances[url]
        except KeyError:
            pass


class ActivityTaskSingleton(type):
    _instances = {}

    # task肯定有task_id, 且唯一
    def __call__(cls, task_id:TaskId, *args, **kwargs):
        if task_id not in cls._instances:
            cls._instances[task_id] = super().__call__(task_id, *args, **kwargs)
        return cls._instances[task_id]
    
    @classmethod
    def clear(cls, task_id:TaskId):
        try:
            del cls._instances[task_id]
        except KeyError:
            pass


ImageTaskSingleton = ActivityTaskSingleton


class BaseTask(object):
    def new_state(self, state: TaskState):
        self._state = state
    
    def ready(self):
        raise NotImplementedError()
    
    def do_task(self):
        return self._state.run(self)
    
    def finish(self):
        raise NotImplementedError()


# 可定义任务状态: stoped -> ready -> stoped , 只有ready状态可run

class TaskState():
    @staticmethod
    def ready(task):
        raise NotImplementedError()
    
    @staticmethod
    def run(task):
        raise NotImplementedError()
    
    @staticmethod
    def stop(task):
        raise NotImplementedError()
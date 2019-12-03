import sense_core as sd
import logging


def init_config(module='sense_push', module_name=''):
    sd.log_init_config(module, sd.config('log_path'), monit_queue='rabbit_monit', use_module_name=module_name)
    logging.getLogger("pika").propagate = False


def build_push_message(action, database, table, data):
    return dict(
        action=action,
        db=database,
        table=table,
        data=data,
    )

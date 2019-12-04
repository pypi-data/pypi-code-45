from config import THREAD_NUM, NICE_PROJECT
from core.worker_pool import MessageThreadPool

profession_message_pool = MessageThreadPool(NICE_PROJECT, THREAD_NUM)
MESSAGE_POOLS = {NICE_PROJECT: profession_message_pool}

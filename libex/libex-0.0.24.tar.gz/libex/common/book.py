  
import logging

logger = logging.getLogger(__name__)

def update_book(depths,size,asks,bids,timestamp):

    logger.debug(f"update book, depths:{depths} , asks:{asks} , bids:{bids} , timestamp:{timestamp}\n")

    curr_asks = depths.setdefault('asks',[])
    curr_bids = depths.setdefault('bids',[])

    for item in asks:

        arr = [n for n in curr_asks if n[0] != item[0]]

        if item[1] != '0' and item[1] != 0:
            arr.append(item)

        curr_asks = arr

        
    for item in bids: 

        arr = [n for n in curr_bids if n[0] != item[0]]

        if item[1] != '0' and item[1] != 0:
            arr.append(item)

        curr_bids = arr

    sorted_asks = sorted(curr_asks, key=lambda a: a[0])[0:size]  # 按每个元素的第一个数据排序
    depths['asks'] = sorted_asks

    sorted_bids = sorted(curr_bids, key=lambda a: a[0],reverse=True)[0:size]  # 按每个元素的第一个数据排序
    depths['bids'] = sorted_bids
  
    depths['ts'] = timestamp
import os
from queue import Queue
from threading import Thread, Lock, current_thread
from urllib import parse

import numpy as np
from requests import Session
from tqdm import tqdm

APP_ID = 266719
# APP_ID = 265486

BASE_URL_PAN = 'http://pan.baidu.com/rest/2.0/pcs'
BASE_URL_CPS = 'http://pcs.baidu.com/rest/2.0/pcs'

BASE_URL_CPS_NEW = 'http://c.pcs.baidu.com/rest/2.0/pcs'


class SuperDownloaderBak1(object):
    """HTTP下载较大文件的工具
    """

    def __init__(self, url, session, save_path, thread_num=45, queue_size=10, chunk=102400):
        """
        :param url: 资源链接
        :param session: 构造好上下文的session
        :param save_path: 保存路径
        :param thread_num: 下载线程数
        :param queue_size: 队列的大小，默认10
        :param chunk: 每个线程下载的块大小
        """
        self.url = url
        self.session = session
        self.save_path = save_path
        self.thread_num = thread_num
        self.queue = Queue(queue_size)
        self.file_size = self._content_length()
        self.position = 0  # 当前的字节偏移量
        self.chunk = chunk
        self.mutex = Lock()  # 资源互斥锁
        self.flags = [False] * self.thread_num

    def download(self):
        with open(self.save_path, 'wb') as fp:
            threads = []
            for i in range(self.thread_num):
                p = Thread(target=self._produce, name='%d' % i)
                threads.append(p)
                p.start()
            c = Thread(target=self._consume, args=(fp,), name='consumer')
            threads.append(c)
            c.start()
            for t in threads:
                t.join()

    def _produce(self):
        interval = [0, 0]
        while True:
            if self.mutex.acquire():
                if self.position > self.file_size - 1:
                    self.flags[int(current_thread().getName())] = True
                    self.mutex.release()
                    return
                interval = (self.position, self.position + self.chunk)
                self.position += (self.chunk + 1)
                self.mutex.release()
            resp = self.session.get(
                self.url, headers={'Range': 'bytes=%s-%s' % interval})
            if not self.queue.full():
                self.queue.put((interval, resp.content))

    def _consume(self, fp):
        while True:
            if all(self.flags) and self.queue.empty():
                return
            if not self.queue.empty():
                item = self.queue.get()
                fp.seek(item[0][0])
                fp.write(item[1])

    def _content_length(self):
        """
        发送head请求获取content-length
        """
        resp = self.session.head(self.url)
        length = resp.headers.get('content-length')
        if length:
            return int(length)
        else:
            raise Exception('%s don\'t support Range' % self.url)


class SuperDownloaderM(object):
    """
    HTTP下载较大文件的工具
    """

    def __init__(self, session, thread_num=10, queue_size=10, chunk=1024 * 1024):
        """
        :param session: 构造好上下文的session
        :param thread_num: 下载线程数
        :param queue_size: 队列的大小，默认10
        :param chunk: 每个线程下载的块大小
        """
        # self.url = url
        self.session = session

        self.thread_num = thread_num
        self.queue = Queue(queue_size)

        self.position = 0  # 当前的字节偏移量
        self.chunk = chunk
        self.mutex = Lock()  # 资源互斥锁
        self.flags = [False] * self.thread_num

    def download_list(self, meta_list=None, overwrite=True):
        """
        批量下载多个文件
        :param meta_list:
        :param overwrite: 是否覆盖
        :return:
        """
        for meta in meta_list:
            self.download(meta, overwrite=overwrite)
        pass

    def download(self, meta, overwrite=True):
        """
        下载单个文件
        如果单个文件大小小于100MB,启动单线程下载，否则启动多线程下载

        :param overwrite: 是否覆盖
        :param meta:       文件参数，需包含下列参数
               size        文件大小  byte
               url         下载路径
               file_name   保存文件名
               local_path  本地保存路径，包含文件名
        :return:
        """

        file_size = meta['size']
        local_path = meta['local_path']
        file_name = os.path.basename(local_path)

        self.init_path(meta['local_path'])
        if os.path.exists(local_path):
            if not overwrite and os.path.getsize(local_path) / file_size > 0.99:
                print(file_name + ' has been exist!')
                return True

        if meta['size'] < 10 * 1024 * 1024:
            return self.download_single(meta)
        else:
            return self.download_multi(meta)

    def download_single(self, meta):
        """
        单线程下载单个文件
        :param meta:  
        :return: 
        """
        url = meta['url']
        file_size = meta['size']
        local_path = meta['local_path']
        file_name = os.path.basename(local_path)
        if os.path.exists(local_path):
            first_byte = os.path.getsize(local_path)
        else:
            first_byte = 0

        self.init_path(local_path)

        position = first_byte

        mode = 'ab' if first_byte > 0 else 'wb'
        with open(local_path, mode=mode) as f:
            with tqdm(initial=np.round(first_byte / self.chunk, 2),
                      total=np.round(file_size / self.chunk, 2),
                      # unit_scale=True,
                      unit='MB',
                      desc=file_name) as pbar:
                while position < file_size:
                    interval = (position, position + self.chunk)
                    position += (self.chunk + 1)

                    time = 3
                    while time > 0:
                        try:
                            resp = self.session.get(url, headers={'Range': 'bytes=%s-%s' % interval})
                            f.write(resp.content)
                            pbar.update(1)
                            break
                        except Exception as e:
                            time -= 1
                            print(e)

        return True

    def download_multi(self, meta):
        """
        多线程下载单个文件
        :param meta:
        :return:
        """
        with open(meta['local_path'], 'wb') as fp:
            threads = []
            for i in range(self.thread_num):
                p = Thread(target=self._produce, args=(meta,), name='%d' % i)
                threads.append(p)
                p.start()
            c = Thread(target=self._consume, args=(fp, meta,), name='consumer')
            threads.append(c)
            c.start()
            for t in threads:
                t.join()

    def _produce(self, meta):
        interval = [0, 0]

        while True:
            if self.mutex.acquire():
                if self.position > meta['size'] - 1:
                    self.flags[int(current_thread().getName())] = True
                    self.mutex.release()
                    return
                interval = (self.position, self.position + self.chunk)
                self.position += (self.chunk + 1)
                self.mutex.release()
            time = 3
            while time > 0:
                try:
                    resp = self.session.get(meta['url'], headers={'Range': 'bytes=%s-%s' % interval})
                    if not self.queue.full():
                        self.queue.put((interval, resp.content))
                    break
                except Exception as e:
                    time -= 1
                    print(e)

    def _consume(self, fp, meta):
        with tqdm(total=np.round(meta['size'] / self.chunk),
                  unit='MB',
                  desc=meta['server_filename']) as pbar:
            while True:
                if all(self.flags) and self.queue.empty():
                    return
                if not self.queue.empty():
                    item = self.queue.get()
                    fp.seek(item[0][0])
                    fp.write(item[1])
                    pbar.update(1)
                    # print(item[0])

    @staticmethod
    def init_path(path):
        local_dir = os.path.dirname(path)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)


class SecretManage(object):
    def __init__(self, key, value=None, path='default', secret_dir='~/.secret', save=True):
        self.key = key
        secret_dir = secret_dir.replace("~", os.environ['HOME'])
        self.secret_path = '{}/{}/.{}'.format(secret_dir, path, key)
        self.value = value
        if self.value is None:
            self.read()
        if save:
            self.write()

    def read(self):
        """
        从文件读取
        """
        if self.value is not None:
            return self.value
        try:
            if os.path.exists(self.secret_path):
                self.value = open(self.secret_path).read()
                print("read from local")
        except Exception as e:
            print("read error ,init {}".format(e))
        return self.value

    def write(self):
        """
        写入到文件
        """
        if self.value is None:
            return
        try:
            secret_dir = os.path.dirname(self.secret_path)
            if not os.path.exists(secret_dir):
                os.makedirs(secret_dir)
            with open(self.secret_path, 'w')as f:
                f.write(self.value)
                print("write to local")
        except Exception as e:
            print('error {}'.format(e))

    def delete_key(self):
        """
        删除
        """
        if os.path.exists(self.secret_path):
            os.remove(self.secret_path)


class BaiDuDrive(object):
    """
    A client for the PCS API.
    官方API https://openapi.baidu.com/wiki/index.php?title=docs/pcs/rest/file_data_apis_list
    """

    def __init__(self, bduss=None, session=None, timeout=None, access_token=None, save=True):
        """
        :param bduss: The value of baidu cookie key `BDUSS`.
        """
        self.secret = SecretManage(key='bduss', value=bduss, path='baidu', save=save)

        self.bduss = self.secret.read()
        self.session = session or Session()

        self.access_token = access_token
        self.timeout = timeout

        self.session.headers.update({'Cookie': 'BDUSS=%s' % self.bduss})

    def quota(self):
        """
        空间配额信息:获取当前用户空间配额信息。

        :return quota: uint64   空间配额，单位为字节。
        :return used: uint64   已使用空间大小，单位为字节。
        """
        return self.request('GET', '/quota', params=dict(method='info'))

    def upload(self, local_path, yun_path, overwrite=True):
        """
        上传单个文件:上传单个文件。百度PCS服务目前支持最大2G的单个文件上传。
        如需支持超大文件（>2G）的断点续传，请参考下面的“分片文件上传”方法。

        注意： 兼容原有域名pcs.baidu.com；使用新域名c.pcs.baidu.com，则提供更快、更稳定的上传服务。

        :param local_path:     本地文件路径（含上传的文件名称）。
        :param yun_path:       云端文件路径（含上传的文件名称）。
        :param overwrite:      是否覆盖同名文件，默认覆盖
        """
        if overwrite:
            ondup = 'overwrite'
        else:
            ondup = 'newcopy'
        params = {
            'method': 'upload',
            'path': yun_path,
            'ondup': ondup
        }
        files = {yun_path: open(local_path, 'rb')}
        res = self.request('POST', '/file', params=params, files=files, base_url=BASE_URL_CPS_NEW)
        print('from {} upload to {} done'.format(local_path, yun_path))
        return res

    def upload_dir(self, local_dir, yun_dir, overwrite=True):
        """
        上传文件夹
        :param local_dir: 本地文件夹
        :param yun_dir:   云端文件夹
        :param overwrite: 是否覆盖
        :return:
        """
        if not os.path.exists(local_dir):
            return True
        self.mkdir(yun_dir)

        for file in os.listdir(local_dir):
            file_path_local = os.path.join(local_dir, file)
            file_path_yun = os.path.join(yun_dir, file)

            if os.path.isdir(file_path_local):
                self.upload_dir(file_path_local, file_path_yun, overwrite=overwrite)
            else:
                self.upload(file_path_local, file_path_yun, overwrite=overwrite)

        return True

    def upload_tmpfile(self, local_path):
        """分片上传—文件分片及上传 :百度PCS服务支持每次直接上传最大2G的单个文件。
        如需支持上传超大文件（>2G），则可以通过组合调用分片文件上传的upload方法和createsuperfile方法实现：

        首先，将超大文件分割为2G以内的单文件，并调用upload将分片文件依次上传；
             其次，调用createsuperfile，完成分片文件的重组。

        除此之外，如果应用中需要支持断点续传的功能，也可以通过分片上传文件并调用createsuperfile接口的方式实现。

        兼容原有域名pcs.baidu.com；使用新域名c.pcs.baidu.com，则提供更快、更稳定的上传服务。

        :param local_path: 本地文件路径（含上传的文件名称）。

        :return md5: string   文件的md5签名。
        """
        params = {
            'method': 'upload',
            'type': 'tmpfile'
        }

        files = {local_path: open(local_path, 'rb')}

        return self.request('POST', '/file', params=params, files=files, base_url=BASE_URL_CPS_NEW)

    def upload_superfile(self, block_list, yun_path, ondup=True):
        """分片上传—合并分片文件  :与分片文件上传的upload方法配合使用，可实现超大文件（>2G）上传，同时也可用于断点续传的场景。


        :param block_list: 数组，数组的取值为子文件内容的MD5；子文件至少两个，最多1024个。
        :param yun_path:  云端文件路径（含上传的文件名称）。
        :param ondup: 是否覆盖同名文件，默认覆盖

        """
        params = {
            'method': 'createsuperfile',
            'path': yun_path,
            'param': {"block_list": block_list},
            'ondup': ondup,
        }

        return self.request('POST', '/file', params=params)

    def upload_bigfile(self, local_path, yun_path, ondup=True):
        # TODO 大文件分割单个小文件
        paths = local_path.split('')

        block_list = []
        for path in paths:
            res = self.upload_tmpfile(path)
            block_list.append(res['md5'])
        return self.upload_superfile(block_list, yun_path, ondup)
        pass

    def download(self, yun_path, local_path=None, overwrite=True):
        """下载文件
        当local_path为None时，文件会保存在工作目录下，文件名默认为网盘的文件名。
        当local_path以/结尾时，文件名默认为网盘的文件名
        :param overwrite:     是否覆盖
        :param yun_path:      网盘下的文件路径
        :param local_path:    保存本地的文件路径
        """
        yun_dir, yun_filename = os.path.split(yun_path)
        cwd = os.getcwd()
        if local_path is None:
            local_dir = cwd
            local_filename = yun_filename
        else:
            local_dir, local_filename = os.path.split(local_path)
            if not local_dir:
                local_dir = os.getcwd()
            if not os.path.exists(local_dir):
                os.makedirs(local_dir)
            if not local_filename:
                local_filename = yun_filename
        local_path = os.path.join(local_dir, local_filename)

        params = {
            'method': 'download',
            'app_id': APP_ID,
            'path': yun_path
        }
        query_string = parse.urlencode(params)

        url = BASE_URL_CPS + '/file?%s' % query_string

        meta = self.meta(yun_path)
        if len(meta) == 0:
            return
        meta = meta[0]
        meta.update({
            "url": url,
            "local_path": local_path
        })
        super_downloader = SuperDownloaderM(self.session)
        super_downloader.download(meta, overwrite=overwrite)

        return True

    def download_dir(self, yun_dir, local_dir=None, overwrite=True):
        """下载文件
        当local_path为None时，文件会保存在工作目录下，文件名默认为网盘的文件名。
        当local_path以/结尾时，文件名默认为网盘的文件名
        :param overwrite:     是否覆盖
        :param yun_dir:       网盘下的文件路径
        :param local_dir:     保存本地的文件路径
        """

        cwd = os.getcwd()
        if local_dir is None:
            local_dir = cwd
        local_dir = os.path.join(local_dir, os.path.split(yun_dir)[-1])

        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        files = self.list_deep(yun_dir, max_depth=3)

        paths = []
        start_ = '###'
        for file in files:
            if file['isdir'] == 1:
                continue
            path = start_ + file['path']

            path = path.replace(start_ + yun_dir, local_dir)

            params = {
                'method': 'download',
                'app_id': APP_ID,
                'path': file['path']
            }
            url = BASE_URL_CPS + '/file?%s' % parse.urlencode(params)

            file.update({
                "from": file['path'],
                "url": url,
                "local_path": path
            })
            paths.append(file)

        print(paths)
        print(local_dir)

        for i in range(1, 4):
            path = paths[i]
            # print(path)
            # super_downloader = SuperDownloader(path['url'], self.session, path['local_path'], file_meta=path)
            super_downloader = SuperDownloaderM(self.session)
            # super_downloader.download_single(path)
            # super_downloader.download_multi(path)
            super_downloader.download(path, overwrite=overwrite)

        return True

    def mkdir(self, yun_path):
        """创建目录
        :param yun_path:
        创建目录:为当前用户创建一个目录。
        """
        params = {
            'method': 'mkdir',
            'path': yun_path
        }
        return self.request('POST', '/file', params=params)

    def meta(self, yun_path):
        """
        获取单个文件/目录的元信息:获取单个文件或目录的元信息。

        :param yun_path:需要获取文件属性的目录，以/开头的绝对路径。如：/apps/album/a/b/c
         注意：: 路径长度限制为1000   非必传   文件名或路径名开头结尾不能是“.”或空白字符，空白字符包括: \r, \n, \t, 空格, \0, \x0B


        :return fs_id: uint64        文件或目录在PCS的临时唯一标识ID。
        :return path: string         文件或目录的绝对路径。
        :return ctime: uint          文件或目录的创建时间。
        :return mtime: uint          文件或目录的最后修改时间。
        :return block_list: string   文件所有分片的md5数组JSON字符串。
        :return size: uint64         文件大小（byte）。
        :return isdir: uint          是否是目录的标识符：“0”为文件 : “1”为目录
        :return ifhassubdir: uint    是否含有子目录的标识符：   “1”表示有子目录
        :return:
        """
        params = {
            'method': 'meta',
            'path': yun_path
        }
        res = self.request('GET', '/file', params=params)
        return res.get('list', [])

    def meta_list(self, paths):
        """
        批量获取文件/目录的元信息:批量获取文件或目录的元信息。

        :param paths:   JSON字符串。
        {
        "list":[
            {
                "path":"/apps/album/a/b/c"
            },
            {
                "path":"/apps/album/a/b/d"
            }]
        }

        注意：: 路径长度限制为1000   非必传   文件名或路径名开头结尾不能是“.”或空白字符，空白字符包括: \r, \n, \t, 空格, \0, \x0B


        :return fs_id: uint64   文件或目录在PCS的临时唯一标识id。
        :return path: string   文件或目录的绝对路径。
        :return ctime: uint   文件或目录的创建时间。
        :return mtime: uint   文件或目录的修改时间。
        :return size: uint64   文件大小（byte）。
        :return block_list: string   文件所有分片的md5数组json字符串。
        :return isdir: uint   是否是目录的标识符：
        :return “0”为文件 : “1”为目录   uint
        :return 否: 是否含有子目录的标识符：   “1”表示有子目录
        :return:
        """

        path_list = []
        for path in paths:
            path_list.append({"path": path})

        params = {
            'method': 'meta',
            'param': {'list': path_list}
        }
        res = self.request('POST', '/file', params=params)
        return res.get('list', [])

    def list_deep(self, yun_dir, by='name', order='asc', limit='0-100', depth=0, max_depth=5):
        paths = []

        depth += 1
        if depth > max_depth:
            return paths

        files = self.list(yun_dir, by=by, order=order, limit=limit)
        for file in files:
            file['depth'] = depth
            paths.append(file)
            if file['isdir'] == 1:
                paths.extend(
                    self.list_deep(file['path'], by=by, order=order, limit=limit, depth=depth, max_depth=max_depth))

        return paths

    def list(self, yun_dir, by='name', order='asc', limit='0-100'):
        """
        获取目录下的文件列表:获取目录下的文件列表。

        :param yun_dir:    需要list的目录，以/开头的绝对路径。
        :param by:         排序字段，缺省根据文件类型排序：
                                time（修改时间）
                                name（文件名）
                                size（大小，注意目录无大小）
        :param order:      asc（升序）desc（降序）
        :param limit:      否 返回条目控制，参数格式为：n1-n2。返回结果集的[n1, n2)之间的条目，缺省返回所有条目；n1从0开始。


        :return fs_id: uint64   文件或目录在PCS的临时唯一标识id。
        :return path: string    文件或目录的绝对路径。
        :return ctime: uint     文件或目录的创建时间。
        :return mtime: uint     文件或目录的最后修改时间。
        :return md5: string     文件的md5值。
        :return size: uint64    文件大小（byte）。
        :return isdir: uint     是否是目录的标识符：
        """
        params = {
            'method': 'list',
            'path': yun_dir,

            'by': by,
            'order': order,
            'limit': limit,
        }
        res = self.request('GET', '/file', params=params)

        return res.get('list', [])

    def move(self, path_from, path_to):
        """
        移动单个文件/目录:移动单个文件/目录。

        :param path_from:   源文件地址（包括文件名）。
        :param path_to:     目标文件地址（包括文件名）。


        :return  描述: from   是
        :return 执行move操作成功的源文件地址。: to   是

        """
        params = {
            'method': 'move',
            'from': path_from,
            'to': path_to
        }
        return self.request('POST', '/file', params=params)

    def move_list(self, move_list):
        """
        移动单个文件/目录:移动单个文件/目录。

        :param move_list:   源文件地址和目标文件地址对应的列表。
        [
            {
                "from":"/apps/album/a/b/c",
                "to":"/apps/album/b/b/c"
            },{
                "from":"/apps/album/a/b/d",
                "to":"/apps/album/b/b/d"
            }
        ]


        :return  描述: from   是
        :return 执行move操作成功的源文件地址。: to   是

        """
        params = {
            'method': 'move',
            'param': move_list,
        }
        return self.request('POST', '/file', params=params)

    def copy(self, path_from, path_to):
        """
        复制单个文件/目录:移动单个文件/目录。

        :param path_from:   源文件地址（包括文件名）。
        :param path_to:     目标文件地址（包括文件名）。


        :return  描述: from   是
        :return 执行move操作成功的源文件地址。: to   是

        """
        params = {
            'method': 'copy',
            'from': path_from,
            'to': path_to
        }
        return self.request('POST', '/file', params=params)

    def copy_list(self, move_list):
        """
        复制单个文件/目录:移动单个文件/目录。

        :param move_list:   源文件地址和目标文件地址对应的列表。
        [
            {
                "from":"/apps/album/a/b/c",
                "to":"/apps/album/b/b/c"
            },{
                "from":"/apps/album/a/b/d",
                "to":"/apps/album/b/b/d"
            }
        ]


        :return  描述: from   是
        :return 执行move操作成功的源文件地址。: to   是

        """
        params = {
            'method': 'move',
            'param': move_list,
        }
        return self.request('POST', '/file', params=params)

    def delete(self, yun_path):
        """
        获取单个文件/目录的元信息:获取单个文件或目录的元信息。

        :param yun_path:需要获取文件属性的目录，以/开头的绝对路径。如：/apps/album/a/b/c

        :return:
        """
        params = {
            'method': 'delete',
            'path': yun_path
        }
        return self.request('POST', '/file', params=params)

    def delete_list(self, paths):
        """
        批量获取文件/目录的元信息:批量获取文件或目录的元信息。

        :param paths:   JSON字符串。如：
        [
            "/apps/album/a/b/c",
            "/apps/album/a/b/d"
        ]

        :return:
        """

        path_list = []
        for path in paths:
            path_list.append({"path": path})

        params = {
            'method': 'delete',
            'param': {'list': path_list}
        }
        return self.request('POST', '/file', params=params)

    def get(self, uri, params):
        return self.request('GET', uri, params=params)

    def request(self, method, uri, headers=None, params=None, data=None, files=None, stream=None, base_url=None):
        if base_url is None:
            base_url = BASE_URL_CPS
        if params is None:
            params = {}

        params.update({
            'app_id': APP_ID,
            # 'access_token': self.access_token
        })
        url = base_url + uri
        resp = self.session.request(method, url,
                                    headers=headers,
                                    params=params,
                                    data=data,
                                    files=files,
                                    timeout=self.timeout,
                                    stream=stream)

        return resp.json()

import mxnet as mx
#import multiprocessing as python_multiprocessing
import threading
import itertools
import queue

from .sampler import Sampler, SequentialSampler, RandomSampler, BatchSampler
from .worker import _worker_loop, ExceptionWrapper, get_worker_info

class _MapDatasetFetcher(object):
    def __init__(self, dataset, auto_collation, collate_fn, drop_last):
        self.dataset = dataset
        self.auto_collation = auto_collation
        self.collate_fn = collate_fn
        self.drop_last = drop_last

    def fetch(self, possibly_batched_index):
        if self.auto_collation:
            data = [self.dataset[idx] for idx in possibly_batched_index]
        else:
            data = self.dataset[possibly_batched_index]
        return self.collate_fn(data)

class DataLoader(object):
    r"""
    Data loader. Combines a dataset and a sampler, and provides an iterable over
    the given dataset.

    The :class:`DataLoader` supports both map-style and
    iterable-style datasets with single- or multi-process loading, customizing
    loading order and optional automatic batching (collation) and memory pinning.

    Arguments:
        dataset (Dataset): dataset from which to load the data.
        batch_size (int, optional): how many samples per batch to load
            (default: ``1``).
        shuffle (bool, optional): set to ``True`` to have the data reshuffled
            at every epoch (default: ``False``).
        sampler (Sampler, optional): defines the strategy to draw samples from
            the dataset. If specified, :attr:`shuffle` must be ``False``.
        batch_sampler (Sampler, optional): like :attr:`sampler`, but returns a batch of
            indices at a time. Mutually exclusive with :attr:`batch_size`,
            :attr:`shuffle`, :attr:`sampler`, and :attr:`drop_last`.
        num_workers (int, optional): how many subprocesses to use for data
            loading. ``0`` means that the data will be loaded in the main process.
            (default: ``0``)
        collate_fn (callable, optional): merges a list of samples to form a
            mini-batch of Tensor(s).  Used when using batched loading from a
            map-style dataset.
        pin_memory (bool, optional): If ``True``, the data loader will copy Tensors
            into CUDA pinned memory before returning them.  If your data elements
            are a custom type, or your :attr:`collate_fn` returns a batch that is a custom type,
            see the example below.
        drop_last (bool, optional): set to ``True`` to drop the last incomplete batch,
            if the dataset size is not divisible by the batch size. If ``False`` and
            the size of dataset is not divisible by the batch size, then the last batch
            will be smaller. (default: ``False``)
        timeout (numeric, optional): if positive, the timeout value for collecting a batch
            from workers. Should always be non-negative. (default: ``0``)
        worker_init_fn (callable, optional): If not ``None``, this will be called on each
            worker subprocess with the worker id (an int in ``[0, num_workers - 1]``) as
            input, after seeding and before data loading. (default: ``None``)


    .. warning:: If the ``spawn`` start method is used, :attr:`worker_init_fn`
                 cannot be an unpicklable object, e.g., a lambda function. See
                 :ref:`multiprocessing-best-practices` on more details related
                 to multiprocessing in PyTorch.

    """

    __initialized = False

    def __init__(self, dataset, batch_size=1, shuffle=False, sampler=None,
                 batch_sampler=None, num_workers=0, collate_fn=None,
                 pin_memory=False, drop_last=False, timeout=0,
                 worker_init_fn=None, multiprocessing_context=None):

        if num_workers < 0:
            raise ValueError('num_workers option should be non-negative; '
                             'use num_workers=0 to disable multiprocessing.')

        if timeout < 0:
            raise ValueError('timeout option should be non-negative')

        self.dataset = dataset
        self.num_workers = num_workers
        self.pin_memory = pin_memory
        self.timeout = timeout
        self.worker_init_fn = worker_init_fn
        #self.multiprocessing_context = multiprocessing_context

        if sampler is not None and shuffle:
            raise ValueError('sampler option is mutually exclusive with '
                             'shuffle')

        if batch_sampler is not None:
            # auto_collation with custom batch_sampler
            if batch_size != 1 or shuffle or sampler is not None or drop_last:
                raise ValueError('batch_sampler option is mutually exclusive '
                                 'with batch_size, shuffle, sampler, and '
                                 'drop_last')
            batch_size = None
            drop_last = False
        elif batch_size is None:
            # no auto_collation
            if shuffle or drop_last:
                raise ValueError('batch_size=None option disables auto-batching '
                                 'and is mutually exclusive with '
                                 'shuffle, and drop_last')

        if sampler is None:  # give default samplers
            if shuffle:
                sampler = RandomSampler(dataset)
            else:
                sampler = SequentialSampler(dataset)

        if batch_size is not None and batch_sampler is None:
            # auto_collation without custom batch_sampler
            batch_sampler = BatchSampler(sampler, batch_size, drop_last)

        self.batch_size = batch_size
        self.drop_last = drop_last
        self.sampler = sampler
        self.batch_sampler = batch_sampler

        self.collate_fn = mx.gluon.data.dataloader.default_mp_batchify_fn
        self.__initialized = True

    #@property
    #def multiprocessing_context(self):
    #    return self.__multiprocessing_context

    #@multiprocessing_context.setter
    #def multiprocessing_context(self, multiprocessing_context):
    #    if multiprocessing_context is not None:
    #        if self.num_workers > 0:
    #            if not python_multiprocessing._supports_context:
    #                raise ValueError('multiprocessing_context relies on Python >= 3.4, with '
    #                                 'support for different start methods')

    #            if not isinstance(multiprocessing_context, python_multiprocessing.context.BaseContext):
    #                raise ValueError(('multiprocessing_context option should be a valid context '
    #                                  'object or a string specifying the start method, but got '
    #                                  'multiprocessing_context={}').format(multiprocessing_context))
    #        else:
    #            raise ValueError(('multiprocessing_context can only be used with '
    #                              'multi-process loading (num_workers > 0), but got '
    #                              'num_workers={}').format(self.num_workers))
    #    self.__multiprocessing_context = multiprocessing_context

    def __setattr__(self, attr, val):
        if self.__initialized and attr in ('batch_size', 'batch_sampler', 'sampler', 'drop_last', 'dataset'):
            raise ValueError('{} attribute should not be set after {} is '
                             'initialized'.format(attr, self.__class__.__name__))

        super(DataLoader, self).__setattr__(attr, val)

    def __iter__(self):
        if self.num_workers == 0:
            return _SingleProcessDataLoaderIter(self)
        else:
            return _MultiProcessingDataLoaderIter(self)

    @property
    def _auto_collation(self):
        return self.batch_sampler is not None

    @property
    def _index_sampler(self):
        if self._auto_collation:
            return self.batch_sampler
        else:
            return self.sampler

    def __len__(self):
        return len(self._index_sampler)  # with iterable-style dataset, this will error


class _BaseDataLoaderIter(object):
    def __init__(self, loader):
        self._dataset = loader.dataset
        self._dataset_kind = 0
        self._auto_collation = loader._auto_collation
        self._drop_last = loader.drop_last
        self._index_sampler = loader._index_sampler
        self._num_workers = loader.num_workers
        self._pin_memory = loader.pin_memory
        self._timeout = loader.timeout
        self._collate_fn = loader.collate_fn
        self._sampler_iter = iter(self._index_sampler)
        self._base_seed = 0

    def __iter__(self):
        return self

    def _next_index(self):
        return next(self._sampler_iter)  # may raise StopIteration

    def __next__(self):
        raise NotImplementedError

    def __len__(self):
        return len(self._index_sampler)

    def __getstate__(self):
        raise NotImplementedError("{} cannot be pickled", self.__class__.__name__)


class _SingleProcessDataLoaderIter(_BaseDataLoaderIter):
    def __init__(self, loader):
        super(_SingleProcessDataLoaderIter, self).__init__(loader)
        assert self._timeout == 0
        assert self._num_workers == 0

        self._dataset_fetcher = _MapDatasetFetcher(
            self._dataset, self._auto_collation, self._collate_fn, self._drop_last)

    def __next__(self):
        index = self._next_index()  # may raise StopIteration
        data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
        #if self._pin_memory:
        # TODO
        return data

    next = __next__  # Python 2 compatibility


class _MultiProcessingDataLoaderIter(_BaseDataLoaderIter):
    r"""Iterates once over the DataLoader's dataset, as specified by the sampler"""
    def __init__(self, loader):
        super(_MultiProcessingDataLoaderIter, self).__init__(loader)

        assert self._num_workers > 0

        #if loader.multiprocessing_context is None:
        #    multiprocessing_context = python_multiprocessing
        #else:
        #    multiprocessing_context = loader.multiprocessing_context
        import dask
        multiprocessing_context = dask.multiprocessing.get_context()

        self._worker_init_fn = loader.worker_init_fn
        self._worker_queue_idx_cycle = itertools.cycle(range(self._num_workers))
        self._worker_result_queue = multiprocessing_context.Queue()
        self._worker_pids_set = False
        self._shutdown = False
        self._send_idx = 0  # idx of the next task to be sent to workers
        self._rcvd_idx = 0  # idx of the next task to be returned in __next__
        self._task_info = {}
        self._tasks_outstanding = 0  # always equal to count(v for v in task_info.values() if len(v) == 1)
        self._workers_done_event = multiprocessing_context.Event()

        self._index_queues = []
        self._workers = []

        self._workers_status = []
        for i in range(self._num_workers):
            index_queue = multiprocessing_context.Queue()
            # index_queue.cancel_join_thread()
            w = multiprocessing_context.Process(
                target=_worker_loop,
                args=(self._dataset_kind, self._dataset, index_queue,
                      self._worker_result_queue, self._workers_done_event,
                      self._auto_collation, self._collate_fn, self._drop_last,
                      self._base_seed + i, self._worker_init_fn, i, self._num_workers))
            w.daemon = True
            w.start()
            self._index_queues.append(index_queue)
            self._workers.append(w)
            self._workers_status.append(True)

        #if self._pin_memory:
        #    self._pin_memory_thread_done_event = threading.Event()
        #    self._data_queue = queue.Queue()
        #    pin_memory_thread = threading.Thread(
        #        target=_utils.pin_memory._pin_memory_loop,
        #        args=(self._worker_result_queue, self._data_queue,
        #              torch.cuda.current_device(),
        #              self._pin_memory_thread_done_event))
        #    pin_memory_thread.daemon = True
        #    pin_memory_thread.start()
        #    # Similar to workers (see comment above), we only register
        #    # pin_memory_thread once it is started.
        #    self._pin_memory_thread = pin_memory_thread
        #else:
        self._data_queue = self._worker_result_queue

        self._worker_pids_set = True

        # prime the prefetch loop
        for _ in range(2 * self._num_workers):
            self._try_put_index()

    def _try_get_data(self, timeout=5.0):
        try:
            data = self._data_queue.get(timeout=timeout)
            return (True, data)
        except Exception as e:
            # At timeout and error, we manually check whether any worker has
            # failed. Note that this is the only mechanism for Windows to detect
            # worker failures.
            failed_workers = []
            for worker_id, w in enumerate(self._workers):
                if self._workers_status[worker_id] and not w.is_alive():
                    failed_workers.append(w)
                    self._shutdown_worker(worker_id)
            if len(failed_workers) > 0:
                pids_str = ', '.join(str(w.pid) for w in failed_workers)
                raise RuntimeError('DataLoader worker (pid(s) {}) exited unexpectedly'.format(pids_str))
            if isinstance(e, queue.Empty):
                return (False, None)
            raise

    def _get_data(self):
        if self._timeout > 0:
            success, data = self._try_get_data(self._timeout)
            if success:
                return data
            else:
                raise RuntimeError('DataLoader timed out after {} seconds'.format(self._timeout))
        #elif self._pin_memory:
        #    while self._pin_memory_thread.is_alive():
        #        success, data = self._try_get_data()
        #        if success:
        #            return data
        #    else:
        #        # while condition is false, i.e., pin_memory_thread died.
        #        raise RuntimeError('Pin memory thread exited unexpectedly')
        #    # In this case, `self._data_queue` is a `queue.Queue`,. But we don't
        #    # need to call `.task_done()` because we don't use `.join()`.
        #else:
        while True:
            success, data = self._try_get_data()
            if success:
                return data

    def __next__(self):
        while True:
            while self._rcvd_idx < self._send_idx:
                info = self._task_info[self._rcvd_idx]
                worker_id = info[0]
                if len(info) == 2 or self._workers_status[worker_id]:  # has data or is still active
                    break
                del self._task_info[self._rcvd_idx]
                self._rcvd_idx += 1
            else:
                # no valid `self._rcvd_idx` is found (i.e., didn't break)
                self._shutdown_workers()
                raise StopIteration

            # Now `self._rcvd_idx` is the batch index we want to fetch

            # Check if the next sample has already been generated
            if len(self._task_info[self._rcvd_idx]) == 2:
                data = self._task_info.pop(self._rcvd_idx)[1]
                return self._process_data(data)

            assert not self._shutdown and self._tasks_outstanding > 0
            idx, data = self._get_data()
            self._tasks_outstanding -= 1

            if idx != self._rcvd_idx:
                # store out-of-order samples
                self._task_info[idx] += (data,)
            else:
                del self._task_info[idx]
                return self._process_data(data)

    next = __next__  # Python 2 compatibility

    def _try_put_index(self):
        assert self._tasks_outstanding < 2 * self._num_workers
        try:
            index = self._next_index()
        except StopIteration:
            return
        for _ in range(self._num_workers):  # find the next active worker, if any
            worker_queue_idx = next(self._worker_queue_idx_cycle)
            if self._workers_status[worker_queue_idx]:
                break
        else:
            # not found (i.e., didn't break)
            return

        self._index_queues[worker_queue_idx].put((self._send_idx, index))
        self._task_info[self._send_idx] = (worker_queue_idx,)
        self._tasks_outstanding += 1
        self._send_idx += 1

    def _process_data(self, data):
        self._rcvd_idx += 1
        self._try_put_index()
        if isinstance(data, ExceptionWrapper):
            data.reraise()
        return data

    def _shutdown_worker(self, worker_id):
        assert self._workers_status[worker_id]

        q = self._index_queues[worker_id]
        # Indicate that no more data will be put on this queue by the current
        # process.
        q.put(None)

        self._workers_status[worker_id] = False

    def _shutdown_workers(self):
        if not self._shutdown:
            self._shutdown = True
            try:
                #if hasattr(self, '_pin_memory_thread'):
                #    # Use hasattr in case error happens before we set the attribute.
                #    self._pin_memory_thread_done_event.set()
                #    self._worker_result_queue.put((None, None))
                #    self._pin_memory_thread.join()
                #    self._worker_result_queue.close()

                # Exit workers now.
                self._workers_done_event.set()
                for worker_id in range(len(self._workers)):
                    if self._workers_status[worker_id]:
                        self._shutdown_worker(worker_id)
                for w in self._workers:
                    w.join()
                for q in self._index_queues:
                    q.cancel_join_thread()
                    q.close()
            finally:
                if self._worker_pids_set:
                    self._worker_pids_set = False

    def __del__(self):
        self._shutdown_workers()

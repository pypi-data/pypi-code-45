from tqdm.auto import tqdm
from typing import List, Callable, Dict, Generator
from .utils import get_level_description, cached, uncached, get_holdout_key
import gc


def empty_generator(*args, **kwargs):
    return []


def are_holdouts_complete(
    holdouts: List,
    cache_dir: str,
    results_directory: str,
    skip: Callable[[str, Dict, str], bool],
    hyper_parameters: Dict = None,
    level: int = 0,
    verbose: bool = True
):
    for number, (_, parameters, _) in enumerate(tqdm(holdouts, disable=not verbose, desc=get_level_description(level))):
        key = get_holdout_key(cache_dir, **parameters,
                              level=level, number=number)
        if key is None or skip(key, hyper_parameters, results_directory):
            return False
    return True


def _holdouts_generator(*dataset: List, holdouts: List, cacher: Callable, cache_dir: str = None, skip: Callable[[str, Dict, str], bool] = None, level: int = 0, verbose: bool = True):
    """Return validation dataset, its key and another holdout generator.
        dataset, iterable of datasets to generate holdouts from.
        holdouts:List, list of holdouts callbacks.
        cacher:Callable, function used to store the cache.
        cache_dir:str=".holdouts", the holdouts cache directory.
        skip:Callable[str, bool], the callback for choosing to load or not a given holdout.
        level:int=0, the level of the current holdout.
        verbose:bool=True, wethever to show loading bars or not.
    """
    if holdouts is None:
        return None

    def generator(results_directory: str = None, hyper_parameters: Dict = None):
        if cache_dir is not None and results_directory is None:
            raise ValueError("Parameter results_directory cannot be None when using cache!")
        for number, (outer, parameters, inner) in enumerate(tqdm(holdouts, disable=not verbose, desc=get_level_description(level))):
            if cache_dir:
                key = get_holdout_key(cache_dir, **parameters,
                                      level=level, number=number)
            if cache_dir is not None and skip is not None and key is not None and skip(key, hyper_parameters, results_directory):
                yield (None, None), key, empty_generator
            else:
                gc.collect()
                (train, test), key = cacher(outer, dataset, cache_dir,
                                            **parameters, level=level, number=number)
                gc.collect()
                if train is None:
                    yield (None, None), key, empty_generator
                else:
                    yield (train, test), key, _holdouts_generator(
                        *train,
                        holdouts=inner,
                        cacher=cacher,
                        cache_dir=cache_dir,
                        skip=skip,
                        level=level+1,
                        verbose=verbose
                    )
    return generator


def _remove_key(generator: Generator):
    if generator is None:
        return None

    def filtered(results_directory: str = None, hyper_parameters: Dict = None):
        for values, _, inner in generator(hyper_parameters, results_directory):
            yield values, _remove_key(inner)
    return filtered


def holdouts_generator(*dataset: List, holdouts: List, verbose: bool = True):
    """Return validation dataset, its key and another holdout generator
        dataset, iterable of datasets to generate holdouts from.
        holdouts:List, list of holdouts callbacks.
        verbose:bool=True, wethever to show loading bars or not.
    """
    return _remove_key(_holdouts_generator(*dataset, holdouts=holdouts, cacher=uncached, verbose=verbose))


def cached_holdouts_generator(*dataset: List, holdouts: List, cache_dir: str, skip: Callable[[str, Dict, str], bool] = None, verbose: bool = True):
    """Return validation dataset, its key and another holdout generator
        dataset, iterable of datasets to generate holdouts from.
        holdouts:List, list of holdouts callbacks.
        cache_dir:str, the holdouts cache directory.
        skip:Callable[str, bool], the callback for choosing to load or not a given holdout.
        verbose:bool=True, wethever to show loading bars or not.
    """
    return _holdouts_generator(*dataset, holdouts=holdouts, cacher=cached, cache_dir=cache_dir, skip=skip, verbose=verbose)

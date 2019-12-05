from setuptools import setup, find_packages
import os
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


def _strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            _strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]


def reqs(*f):
    """Parse requirement file.
    Example:
        reqs('default.txt')          # requirements/default.txt
        reqs('extras', 'redis.txt')  # requirements/extras/redis.txt
    Returns:
        List[str]: list of requirements specified in the file.
    """
    return [req for subreq in _reqs(*f) for req in subreq]

requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'default.txt'), session=PipSession())

setup(
    author='Seidu Abdulai',
    name='micro_ussd_airflow_engine',
    version='0.1.1',
    packages=find_packages(exclude=('ussd_engine',)),
    download_url='https://github.com/seidu626/ussd_engine/archive/v0.1.tar.gz',
    url='https://github.com/seidu626/ussd_engine',
    install_requires=[str(requirement.req) for requirement in requirements],
    include_package_data=True,
    license='MIT',
    author_email='seidu.abdulai@hotmail.com',
    description='Ussd Airflow Library'
)

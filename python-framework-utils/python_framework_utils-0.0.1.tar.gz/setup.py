try:
    from setuptools import setup
except:
    from distutils.core import setup
import setuptools

setup(
    name='python_framework_utils',
    author='kingon',
    version='0.0.1',
    description='Python常用工具类整合框架',
    long_description='Simpler to use python implement any servers. ',
    author_email='521274311@qq.com',
    url='https://gitee.com/kingons/python_framework_utils',
    packages=setuptools.find_packages(),
    install_requires= [
        'fake-useragent>=0.1.11',
        'PyMySQL>=0.9.3',
        'numpy>=1.17.4',
        'moviepy>=1.0.1',
        'Pillow>=6.2.1',
        'requests>=2.22.0',
        'urllib3>=1.25.7',
        'bs4>=0.0.1',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    zip_safe=True,
)
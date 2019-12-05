from distutils.core import setup

requirements = ['lxml>=4.4.2', 'numpy>=1.17.4',
                'Pillow>=6.2.1', 'scipy>=1.3.3']

setup(
    name='boxaug',
    version='0.1.1',
    packages=['boxaug'],
    license='MIT License',
    install_requires=requirements
)

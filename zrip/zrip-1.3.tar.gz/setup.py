from setuptools import setup, find_packages

setup(
    name='zrip',
    version='1.3',
    url='https://github.com/zcdzcdzcd',
    description='rip',
    author='zengcd',
    author_email="zcd0712@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['zrip = core.Main:main']
    },

    python_requires='>=3.7',
    install_requires=[

        'matplotlib==3.0.3',
        'networkx==2.2',
        'setuptools==41.2.0',
        'Pillow==6.2.1'
    ],
)

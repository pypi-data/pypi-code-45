from setuptools import setup
setup(
    name='mc_sokect',
    version='0.0.1',
    author='Hugn_王海涛',
    author_email='wang1183478375@outlook.com',
    url ='https://www.coding4fun.com.cn/',
    install_requires=['urllib3>=1.25.7'
                      ],
    data_files=[('',['mc_sokect.py'])
                ],
    include_package_data = True, 
    zip_safe=False,
    )
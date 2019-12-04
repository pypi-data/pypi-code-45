from distutils.core import setup

setup(
    name='commontaskz',
    packages=['commontaskz'],
    version='0.3.1',
    license='MIT',
    description='Common Prefect Tasks to query systems & process results',
    author='Aliza Rayman',  # Type in your name
    author_email='aliza.rayman@zirra.com',  # Type in your E-Mail
    url='https://github.com/aliza-miller/commontaskz',  # Provide either the link to your github or to your website
    download_url='https://github.com/aliza-miller/commontaskz/archive/v0.3.1.tar.gz',  # I explain this later on
    keywords=['TASKS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'slack',
        'prefect',
        'datetime',
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
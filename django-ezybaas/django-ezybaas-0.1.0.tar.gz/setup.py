import os
from setuptools import find_packages, setup
# from ezybaas import config 

with open(os.path.join(os.path.dirname(__file__), '../README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ezybaas',
    version='0.1.0',
    # package_dir={'':'src'},
    # python_requires='>=3.6',
    # python_requires='>=3.6',
    packages=find_packages(exclude=("ezybaasmain",)),
    install_requires=[
                      "Django>=2",
                      "djangorestframework>=3",
                      "django-rest-swagger>=2"
    ],
    include_package_data=True,
    license='Apache License',
    description="Easiest BaaS. Idea to APIs instantly on SQL DBs!",
    long_description=README,
    long_description_content_type="text/markdown",
    platforms=['any'],
    url='https://www.ezybaas.com/',
    author='Bhavik Shah',
    author_email='bhavik@susthitsoft.com',
    keywords=['django', 'rest', 'database', 'api', 'baas', 'backed'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        
    ],
)

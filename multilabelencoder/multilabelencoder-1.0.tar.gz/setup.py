from setuptools import setup
setup(  name = 'multilabelencoder',
        version = "1.0",
        license = 'MIT',
        description = 'Labelencoder for many pandas dataframe columns package',
#        scripts=['multilabelencoder.py'] ,
        packages = ['multilabelencoder'],
#        package_data = {'hmglib': ['readme.txt']},
        install_requires = ['sklearn'],
        zip_safe = False,
        author = "HMG - Team Big Data & AI",
        author_email = 'data@handelsblattgroup.com',
        maintainer = "Emna Jaoua",
        maintainer_email = "E.Jaoua@handelsblattgroup.com",
        dependency_links= ['']
     )
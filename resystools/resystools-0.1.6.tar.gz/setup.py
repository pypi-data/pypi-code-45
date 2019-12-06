
import setuptools

setuptools.setup(
  name = 'resystools',      
  packages=setuptools.find_packages(),
  data_files = [('resystools', ['explicite/Data/ml-1m/*.dat','Data/ml-100k/*.base']),
                ('resystools', ['implicite/Data/*' ])], 
  version = '0.1.6',     
  license='MIT',        
  description = 'a lib with some recommendation algorithms', 
  author = 'Trong Duc Le',                 
  author_email = 'trongduclebk@gmail.com',     
  url = 'https://github.com/DucLeTrong/resystools',   
  download_url = '',   
  keywords = ['RECOMMENDATION', 'RECOMMENDER'], 
  install_requires=[        
          'sklearn',
          'pandas',
          'numpy'
      ],
  classifiers=[
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
# if __name__ == '__main__':
#     setup(**setup_args, install_requires=install_requires)
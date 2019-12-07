import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pttk',
    version='0.0.3',
    author='Xiaobo Li',
    author_email='xiaobo.li.ai@gmail.com',
    description='Post-Training Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leesusu/post-training-toolkit.git',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

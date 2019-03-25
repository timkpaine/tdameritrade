from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tdameritrade',
    version='0.0.7',
    description='APIs for TD Ameritrade',
    long_description=long_description,
    url='https://github.com/timkpaine/tdameritrade',
    download_url='https://github.com/timkpaine/tdameritrade/archive/v0.0.7.tar.gz',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='finance data',
    packages=find_packages(exclude=[]),
    entry_points={
        'console_scripts': ['tdameritrade-auth = tdameritrade.auth:main']
    }
)

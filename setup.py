from setuptools import setup, find_packages
from codecs import open
import io
import os
import os.path

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = 'tdameritrade'


def get_version(file, name='__version__'):
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]

version = get_version(pjoin(here, name, '_version.py'))

with open(pjoin(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'ipython>=7.0.1',
    'pandas>=0.22.0',
    'pillow>=5.3.0',
    'requests>=2.23.0',
    'selenium>=3.141.0',
    'ujson>=1.35',
]

requires_dev = [
    'flake8>=3.7.8',
    'mock',
    'pytest>=4.3.0',
    'pytest-cov>=2.6.1',
    'Sphinx>=1.8.4',
    'sphinx-markdown-builder>=0.5.2',
] + requires

setup(
    name=name,
    version=version,
    description='APIs for TD Ameritrade',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/timkpaine/{name}'.format(name=name),
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='finance data',
    zip_safe=False,
    packages=find_packages(exclude=[]),
    entry_points={
        'console_scripts': ['tdameritrade-auth = tdameritrade.auth:main']
    },
    install_requires=requires,
    extras_require={
        'dev': requires_dev,
    },
)

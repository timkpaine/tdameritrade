from setuptools import setup, find_packages
from codecs import open
import os
import os.path

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = "tdameritrade"

with open(pjoin(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read().replace("\r\n", "\n")

requires = [
    "pandas>=0.22.0",
    "requests>=2.23.0",
]

requires_auth = [
    "selenium>=3.141.0",
]

requires_dev = (
    [
        "black>=23",
        "bump2version>=1.0.0",
        "flake8>=3.7.8",
        "flake8-black>=0.2.1",
        "mock",
        "pytest>=4.3.0",
        "pytest-cov>=2.6.1",
        "Sphinx>=1.8.4",
        "sphinx-markdown-builder>=0.5.2",
    ]
    + requires
    + requires_auth
)

setup(
    name=name,
    version="0.2.1",
    description="APIs for TD Ameritrade",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timkpaine/{name}".format(name=name),
    author="Tim Paine",
    author_email="t.paine154@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="finance data",
    zip_safe=False,
    packages=find_packages(exclude=[]),
    entry_points={"console_scripts": ["tdameritrade-auth = tdameritrade.auth:main"]},
    install_requires=requires,
    extras_require={
        "auth": requires_auth,
        "dev": requires_dev,
    },
)

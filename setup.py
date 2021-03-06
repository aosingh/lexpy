from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

from setuptools import setup, find_packages

from lexpy import __version__

DISTNAME = 'lexpy'

AUTHOR = 'Abhishek Singh'
MAINTAINER = 'Abhishek Singh'
MAINTAINER_EMAIL = 'aosingh@asu.edu'
DESCRIPTION = ('Python package for lexicon.')
LICENSE = 'GNU GPLv3'
URL = 'https://github.com/aosingh/lexpy'
VERSION = __version__

PACKAGES = ['lexpy']


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Text Processing :: Indexing',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS'
]
keywords = 'trie suffix-trees lexicon directed-acyclic-word-graph dawg'


setup(
    name=DISTNAME,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=MAINTAINER_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    packages=find_packages(exclude=("tests",)),
    package_dir={'lexpy': 'lexpy'},
    include_package_data=True,
    classifiers=classifiers,
    keywords=keywords.split(),
)
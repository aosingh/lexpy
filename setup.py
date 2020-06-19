from __future__ import unicode_literals
from __future__ import absolute_import


from setuptools import setup, find_packages

from lexpy import __version__

LONG_DESCRIPTION = 'A lexicon is a data-structure which stores a set of words. ' \
                   'The difference between a dictionary and a lexicon is that in a lexicon there are no values associated with the words. ' \
                   'A lexicon is similar to a list of words or a set, but the internal representation is different and optimized for faster searches(of words, prefixes and wildcard patterns). ' \
                   'Precisely the search time is O(W) where W is the length of the word. ' \
                   'Lexpy is pure python package which implements 2 important lexicon Data-structures Trie and Directed' \
                   'Acyclic Word Graph(DAWG). '
DISTNAME = 'lexpy'

AUTHOR = 'Abhishek Singh'
MAINTAINER = 'Abhishek Singh'
MAINTAINER_EMAIL = 'aosingh@asu.edu'
DESCRIPTION = ('Python package for lexicon.')
LICENSE = 'GNU GPLv3'
URL = 'https://github.com/aosingh/lexpy'
VERSION = __version__

PACKAGES = ['lexpy']

DEPENDENCIES = ['future']

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Text Processing :: Indexing',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
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
    long_description=LONG_DESCRIPTION,
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
    install_requires=DEPENDENCIES,
    include_package_data=True,
    classifiers=classifiers,
    keywords=keywords,
)
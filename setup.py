from setuptools import setup

DISTNAME = 'lexpy'

AUTHOR = 'Abhishek Singh'
MAINTAINER = 'Abhishek Singh'
MAINTAINER_EMAIL = 'aosingh@asu.edu'
DESCRIPTION = ('Python package for lexicons.')
LICENSE = 'GNU GPLv3'
URL = 'https://github.com/aosingh/lexpy'
VERSION = '0.1.1'

PACKAGES = ['lexpy']

classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Text Processing :: Linguistic',
    'Topic :: Text Processing :: Indexing',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 2.7',
]
keywords='trie suffix-trees lexicon directed-acyclic-word-graph dawg'


setup(
    name=DISTNAME,
    author=AUTHOR,
    author_email=MAINTAINER_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    packages = PACKAGES,
    include_package_data=True,
    classifiers=classifiers,
    keywords=keywords,
)
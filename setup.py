"""Setup file for fullqualname."""

from setuptools import setup
from fullqualname import __version__

description = 'Fully qualified names for Python objects'

with open('README.rst') as file:
    long_description = file.read()

_classifiers = [
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ]

keywords = 'introspection'

setup(
    name='fullqualname',
    version=__version__,
    py_modules=['fullqualname'],
    author='Eric Galloway',
    author_email='ericgalloway@gmail.com',
    description=description,
    long_description=long_description,
    url='https://github.com/etgalloway/fullqualname',
    classifiers=_classifiers,
    keywords=keywords,
    )

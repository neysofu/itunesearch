# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import itunesearch

# External resources
# ------------------

with open('README.md') as f:
    README = f.read()

with open('requirements.txt') as f:
	REQUIREMENTS = f.readlines()

setup(
    name=itunesearch.__name__,
    version=itunesearch.__version__,
    description='A majestic Python wrapper for the dreadful iTunes Search APIs.',
    long_description=README,
    author=itunesearch.__author__,
    author_email=itunesearch.__email__,
    url='https://github.com/neysofu/itunesearch',
    license=itunesearch.__license__,
	install_requires=REQUIREMENTS,
	packages=find_packages(),
	test_suite='test' )

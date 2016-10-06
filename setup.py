# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.txt') as f:
    LICENSE = f.read()

setup(
    name='itunesearch',
    version=0.4,
    description='A Python library for surfing the iTunes Store.',
    long_description=README,
    author='Filippo Costa',
    author_email='filippocosta.italy@gmail.com',
    license=LICENSE,
    url='https://github.com/neysofu/itunesearch',
    install_requires=['requests'],
	packages=find_packages(exclude=('tests', 'docs')) )

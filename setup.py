# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='itunesearch',
    version=0.1,
    description='A Python library for surfing the iTunes Store.',
    long_description=readme,
    author='Filippo Costa',
    author_email='filippocosta.italy@gmail.com',
    license=license,
    url='https://github.com/neysofu/itunesearch',
    install_requires=['requests','bs4'],
    packages=['itunesearch-src'])

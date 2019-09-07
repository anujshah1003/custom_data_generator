"""
################################################################################
##                                                                            ##
##        This code is intended for Continental internal research use         ##
##                                                                            ##
##             Copyright 2017 Corp S&T CDS&T AIR CV & Contributors            ##
##                                                                            ##
##             Licensed under the ContiSource License, Version 1.0            ##
##       You may not use this file except in compliance with the License      ##
##                  You may obtain a copy of the License at                   ##
##                                                                            ##
##  http://github.conti.de/pages/ContiSource/ContiForge/documents/CSLicense   ##
##                                                                            ##
##    Software distributed under the License is distributed on AS IS BASIS    ##
##             and WITHOUT WARRANTY, either expressed or implied              ##
##                                                                            ##
################################################################################

Template for setup file, following https://github.com/pypa/sampleproject/blob/master/setup.py

"""

import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

# Get the long description from the README file
with open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)),
                     'README.md')) as f:
    long_description = f.read()

if os.path.isfile('requirements.txt'):
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    install_reqs = parse_requirements('requirements.txt', session='hack')
    # reqs is a list of requirement e.g. ['django==1.5.1', 'mezzanine==1.4.6']
    reqs = [str(ir.req) for ir in install_reqs]
else:
    reqs = ['']

setup(
    name=<insert name>,
    description=
    <insert description>,
    long_description=long_description,
    author=<insert author(s)>,
    author_email=<insert mail(s)>,
    version=<insert version>,
    url=<insert url>,
    license='ContiSource License, Version 1.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Object Detection :: Semantic Segmentation :: Deep Learning :: Computer Vision',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(
    ),  #http://stackoverflow.com/questions/7522250/how-to-include-package-data-with-setuptools-distribute
    entry_points={
        # add entry_points (if applicable)
    },
    keywords=<add keywords>,
    install_requires=reqs, )

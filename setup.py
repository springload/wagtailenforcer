#!/usr/bin/env python

import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


# Hack to prevent "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when setup.py exits
# (see http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass

PY3 = sys.version_info[0] == 3

install_requires = [
    'wagtail>=1.3',
    'django>=1.8',
    'django-password-policies',
    'django-axes',
    'pyclamd',
]

setup(
    name='wagtailenforcer',
    version='1.0.2',
    description='WagtailEnforcer, the Wagtail arm of the law.',
    author='Jordi J. Tablada, Dave Cartwright',
    author_email='jordi@springload.co.nz, dave@springload.co.nz',
    url='https://github.com/springload/wagtailenforcer/',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    install_requires=install_requires,
    zip_safe=False,
)

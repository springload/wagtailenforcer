#!/usr/bin/env python

import sys, os

from wagtail.wagtailcore import __version__


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
    'django-easysettings',
    # 'git+https://github.com/tarak/django-password-policies',
    # 'git+https://github.com/springload/django-axes',
]

setup(
    name='wagtailenforcer',
    version=__version__,
    description='WagtailEnforcer, the Wagtail arm of the law.',
    author='Jordi J. Tablada',
    author_email='jordi@springload.co.nz',
    url='https://github.com/springload/wagtailenforcer/',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    long_description=open('README.md').read(),
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
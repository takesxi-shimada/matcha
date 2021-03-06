#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

ROOT = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(ROOT, 'README')

try:
    with open(README_PATH, 'rb') as fp:
        long_desc = fp.read()
except:
    long_desc = ''

install_requires = [
    'azoth',
    'twitter',
    'bs4',
    ]
test_require = [
    'tox',
    ]


entry_points = """\
[console_scripts]
legacypython-twitter = legacypython.bots.twitterbot:main
legacypython-pypi = legacypython.bots.pypibot:main
"""

from setuptools.command.test import test as TestCommand
import sys

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

setup(
    name='legacypython',
    version='0.1.0',
    url='https://bitbucket.org/takesxi_sximada/legacypython',
    download_url='https://bitbucket.org/takesxi_sximada/legacypython',
    license='BSD',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description='The Python Package Index Twitter Bot',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Esperanto',
        'Natural Language :: Japanese',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,
    packages=find_packages(),
    cmdclass = {'test': Tox},
    entry_points = entry_points,
    )

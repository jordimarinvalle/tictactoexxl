#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import tictactoexxl


class TestTox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        sys.exit(tox.cmdline(self.test_args))


class Setup(object):

    @staticmethod
    def version():
        return tictactoexxl.get_version()

    @staticmethod
    def long_description(filenames=['README.rst']):
        try:
            descriptions = []
            for filename in filenames:
                descriptions.append(open(filename).read())
            return "\n\n".join(descriptions)
        except:
            return ''

setup(
    name='tictactoexxl',
    version='%s' % (Setup.version()),
    description='A tic-tac-toe game with xxl fun',
    long_description='%s' % (Setup.long_description(['README.rst',
                                                     'HISTORY.rst'])),
    author='Jordi Marín Valle',
    author_email='py.jordi@gmail.com',
    url='https://github.com/jordimarinvalle/tictactoexxl',
    license='MIT',
    platforms='all',
    packages=[
        'tictactoexxl',
    ],
    scripts=[
        'tictactoexxl-play.py',
    ],
    extras_require={
        'testing': [
            'pytest',
            'coverage',
            'pytest-cov',
        ],
    },
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'test': TestTox,
    },
    test_suite="tests",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Games/Entertainment :: Board Games',
    ],
    keywords=[
        'tictactoe', 'tictactoexxl', 'game', 'board game',
    ],
)

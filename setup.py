#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = [
    'docopt>=0.6',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='robtex_python',
    version='0.3.1',
    description="Simple python wrapper for the Robtex API.",
    long_description=readme + '\n\n' + history,
    author="Floyd Hightower",
    author_email='',
    url='https://github.com/fhightower/robtex-python',
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'robtex_python=robtex_python.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license=license,
    zip_safe=True,
    keywords='robtex',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

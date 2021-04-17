
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'docopt>=0.6',
    'requests'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='robtex_python',
    version='1.2.0',
    description="Simple python wrapper for the Robtex API.",
    long_description=readme,
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
    license='MIT License',
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

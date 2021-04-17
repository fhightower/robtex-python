*************
Robtex Python
*************

.. image:: https://img.shields.io/pypi/v/robtex_python.svg
        :target: https://pypi.python.org/pypi/robtex_python

.. image:: https://img.shields.io/travis/fhightower/robtex-python.svg
        :target: https://travis-ci.org/fhightower/robtex-python

.. image:: https://codecov.io/gh/fhightower/robtex-python/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/fhightower/robtex-python

.. image:: https://api.codacy.com/project/badge/Grade/8151c710cd704ddeb8575ee6dfbbd96e
        :target: https://www.codacy.com/app/fhightower/robtex-python

Simple python wrapper for the `Robtex API <https://www.robtex.com/api/>`_ .

Installation
============

Stable release
--------------

To install Robtex Python, run this command in your terminal:

.. code-block:: console

    pip install robtex-python

This is the preferred method to install the Robtex API wrapper, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

From sources
------------

The sources for Robtex Python can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/fhightower/robtex-python

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/fhightower/robtex-python/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python3 setup.py install

.. _Github repo: https://github.com/fhightower/robtex-python
.. _tarball: https://github.com/fhightower/robtex-python/tarball/master

Usage
=====

Via Python
----------

You can use Robtex Python in a script as follows:

.. code-block:: python

    import robtex_python
    response = robtex_python.pdns_forward("example.com")

Via Command Line
----------------

You can use Robtex Python as a command-line tool as follows:

.. code-block:: shell

    Usage:
        robtex_python --ip=<ip>
        robtex_python --as=<asn>
        robtex_python --pdns-forward=<hostname>
        robtex_python --pdns-reverse=<ip>
        robtex_python (-h | --help)
        robtex_python --version

Credits
=======

This package was created with Cookiecutter_ and the `fhightower/python-project-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fhightower/python-project-template`: https://github.com/fhightower/python-project-template

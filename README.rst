Simple API
=======================

Description
------------

This is a simple Tornado application with two API endpoints. You need Python 3.7+, pipenv and pre-commit to run it. Other dependencies
will be installed in the virtual environment. In order to fully use Simple API's features you also need a
client-simple-api which connects to API and displays results. It can be found here as well as running instructions in
README_.

.. _README: https://github.com/szpone/client-simple-api/blob/master/README.md




Getting Python3 and pip
-----------------------

Please refer to the Python wiki_. to determine how you should install Python regarding your operating system.

.. _wiki: https://wiki.python.org/moin/BeginnersGuide/Download


If your operating system or Linux distribution is not listed, check wiki. For example for Arch Linux go to Arch wiki.

The same applies to pip_.

.. _pip: https://pip.pypa.io/en/stable/installing/

|


Getting mypy
------------

Mypy is an optional static checker. It can be obtained through pip.

::

    $ pip install mypy

|


Getting pipenv
---------------

Pipenv creates virtual environment and acts as a package bundler. It can be installed in a couple of different ways,
but probably using

::

    $ pip install pipenv



should be sufficient. If not, please refer to the Pipenv documentation_. to find other ways of installing

.. _documentation: https://docs.pipenv.org/en/latest/install/#installing-pipenv

|

Getting pre-commit
------------------

Pre-commit hook in this app allows to format code and check typings. Configuration file is ready, you need just install
pre-commit using pip. For more information visit pre-commit website_.

.. _website: https://pre-commit.com/#intro

Running virtual environment and installing packages
----------------------------------------------------

To turn on virtual environment through pipenv simply type:

::

    $ pipenv shell

To install dependencies you need to run:

::

    $ pipenv install

In order to install any new package use:

::

    $ pipenv install <package-name>



Running mypy
------------

You can typecheck the script just by typing in the console:

::

    $ mypy roman_numeral_converter.py


If you need more information or troubleshooting advice, please refer to the mypy resources_.

.. _resources:  https://mypy.readthedocs.io/en/stable/

|


Running
-------

Firstly you need clone GitHub repository using

::

    $ git clone


and then go into folder you just cloned. Open console there and simply type:

::

    python api.py


This command starts development server.




Running tests
-------------

In the app folder open console and type:

::

    $ python -m tornado.testing tests.py


The results will appear in the console.


SQLALchemy Qubole
==============================

.. image:: https://travis-ci.org/qubole/qds-sdk-py.svg?branch=master
    :target: https://travis-ci.org/qubole/qds-sdk-py
    :alt: Build Status

The SQLAlchemy is the Python SQL Toolkit and Object Relational Mapper. The primary purpose of this is to have a working dialect for Qubole Presto and Hive that can be used with Apache Superset. This uses our JDBC driver to connect to Qubole Presto/Hive.

Installation
------------

Generic
~~~~~~~
* Download the Qubole JDBC driver (version 2.3 or later) from `here <https://docs.qubole.com/en/latest/connectivity-options/use-qubole-drivers/JDBC-driver/download-jdbc-driver.html>`_.
* Set the environment variable QUBOLE_JDBC_JAR_PATH pointing to JDBC JAR location with absolute path

Example:

    ::

        export QUBOLE_JDBC_JAR_PATH=/Users/testuser/qubolejdbc/qds-jdbc-2.3.0.jar

From PyPI
~~~~~~~~~
The SDK is available on `PyPI <https://pypi.python.org/pypi/sqlalchemy-qubole>`_.

::

    $ pip install sqlalchem-qubole

From source
~~~~~~~~~~~
* Get the source code:

  - Clone the project: ``git clone git@github.com:qubole/sqlalchemy-qubole.git``

* Run the following command (may need to do this as root):

  ::

      $ python setup.py install

* Alternatively, if you use virtualenv, you can do this:

  ::

      $ cd sqlalchemy-qubole
      $ virtualenv venv
      $ source venv/bin/activate
      $ python setup.py install


Example of SQLAlchemy URIs to connect to Qubole

* Presto dialect:

  ::

    qubole+presto://presto/presto_cluster?endpoint=https://api.qubole.com;password=<API-TOKEN>;catalog_name=hive

* Hive dialect:

  ::

    qubole+hive://hive/hadoop2?endpoint=https://api.qubole.com;password=<API-TOKEN>

* By default, qubole dialect points to presto.

Default dialect:

  ::

    qubole://presto/presto_cluster?endpoint=https://api.qubole.com;password=<API-TOKEN>;catalog_name=hive

Reporting Bugs and Contributing Code
------------------------------------

* Want to report a bug or request a feature? Please open `an issue <https://github.com/qubole/sqlalchemy-qubole/issues/new>`_.
* Want to contribute? Fork the project and create a pull request with your changes against ``unreleased`` branch.
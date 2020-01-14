The SQLAlchemy is the Python SQL Toolkit and Object Relational Mapper. The primary purpose of this is to have a working dialect for Qubole Presto and Hive that can be used with Apache Superset. 

This uses our JDBC driver to connect to Qubole Presto/Hive.

Please follow below steps to install the sqlalchemy-qubole package:

Download the Qubole JDBC driver (version 2.3 or later) from here
Set the environment variable QUBOLE_JDBC_JAR_PATH pointing to JDBC JAR location with absolute path
	
Example:
export QUBOLE_JDBC_JAR_PATH=/Users/testuser/qubolejdbc/qds-jdbc-2.3.0.jar

Install sqlalchemy-qubole package: <pending>
It’s done. Now, you can use this package in your python code to run Qubole Presto and Hive queries
Connecting to QDS using sqlalchemy-qubole package:

Example of SQLAlchemy URIs to connect to QDS

Presto dialect: qubole+presto://presto/presto_cluster?endpoint=https://api.qubole.com;password=<API-TOKEN>;catalog_name=hive

Hive dialect: 
qubole+hive://hive/hadoop2?endpoint=https://api.qubole.com;password=<API-TOKEN>

By default, qubole dialect points to presto. 

Default dialect:
qubole://presto/presto_cluster?endpoint=https://api.qubole.com;password=<API-TOKEN>;catalog_name=hive

For more JDBC connection properties, Refer https://docs.qubole.com/en/latest/connectivity-options/use-qubole-drivers/JDBC-driver/additional-properties.html#connection-string-properties
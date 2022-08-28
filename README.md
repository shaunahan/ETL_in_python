# Building ETL piplines in Python

I performed two ETL exercises: <br>
1. <b>ETL WorldBank</b>: use SQLite to perform simple ETL tasks with worldbank database.
2. <b> Building ETL_pipelines </b>: created pipelines in python to efficiently extract, transform, and load data into the system. The detailed files below are all located in the folder.

* `extract.py`: create the local directory for saving data, define a function to download a file (zipped) that contains the housing transaction info.
* `tables.py`: use engines and sessions to connect database with SQLAlchemy, tables for raw and cleaned data.
* `transfrom.py`: clean/transform the data (e.g. lowering letters,  date format conversion, data type changes (string to float to int), update values)
* `base.py`: set up engine and session. Base object has metadata about the schema and tables.
* `create_tables.py`: create a table and commmit changes to the PostgreSQL.
* `insights.py`: contains the total number of sales, the sales total, the max sale, the min sale, the avg sales.
* `insights_export.py`: generate monthly insights
* `execute.py`: call main() function 


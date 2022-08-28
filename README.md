# Building ETL piplines in Python

I performed two ETL exercises: <br>

<b>1. ETL WorldBank</b>: use SQLite to perform simple ETL tasks with worldbank database. 
<br>
* Steps:
    1. Connect to a SQLite database called `worldbank.db` and create a table to hold the gdp data.
    2. Create a python function, `extract_line()`. This function reads in a data file one line at a time, run a transformation on that row of data, and then move on to the next row in the file.
    3. Create a function, `transform_indicator_data()`. This function receives a line from the csv file and transforms the data in preparation for a load step.
    4. Create a function, load_indicator_data(), which loads the trasnformed data into the gdp table in the worldbank.db database.
    5. Run the ETL pipeilne & Run a query against the database to make sure everything worked correctly. 

<br>


<b> 2. Building ETL_pipelines </b>: created pipelines in python to efficiently extract, transform, and load data into the system. The detailed files below are all located in the folder. 
<br><br>
* `extract.py`: create the local directory for saving data, define a function to download a file (zipped) that contains the housing transaction info.
* `tables.py`: use engines and sessions to connect database with SQLAlchemy, tables for raw and cleaned data.
* `transfrom.py`: clean/transform the data (e.g. lowering letters,  date format conversion, data type changes (string to float to int), update values)
* `base.py`: set up engine and session. Base object has metadata about the schema and tables.
* `create_tables.py`: create a table and commmit changes to the PostgreSQL.
* `insights.py`: contains the total number of sales, the sales total, the max sale, the min sale, the avg sales.
* `insights_export.py`: generate monthly insights
* `execute.py`: call main() function 


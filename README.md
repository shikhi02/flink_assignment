# FLINK ASSIGNMENT

## JSON SCHEMA

File event_schema.json is https://json-schema.org/ specification for python.

Below is the sample schema that we used in this pipeline and can be altered in the file events_schema.json if required in future:

schema = {
    "event_type" : "integer",
    "event_time" : "string",
    "data" : {
        "user_email" : {"type" : "string"},
        "phone_number" : {"type" : "string"}
        },
    "processing_date" : "string"
}

Function validate_json() will produce an error and print it if the schema doesn't match the required format of any column in the json file which is handled by exception handling in python.



## DIVIDING THE DATASET INTO BATCHES FOR HANDLING LARGE DATASET

The validation is done in batches of 5000 records, keeping in mind the size of file could get extended upto 10 GB, So as to avoid any processing errors.

We can also use any parallel processing frameworks such as PySpark to handle extremely large datasets.



## MYSQL DATABASE INSERTION

The .db_config_flink file consist of sample mysql database credentials (the dot(.) notation is used for hidden files).

A sample file is present in the codebase which ideally should not be present in codebase and should be kept somewhere in server with dot(.) notation so as to keep it hidden.

### NOTE: .db_config_flink file's credentials should be replaced by a proper working mysql database connection details so as to run the whole pipeline without failure. Also a table should be created in the database with required columns and same should be replaced by table_name in INSERT AND COUNT queries in the main function.

Each validated row is being inserted into a sample mysql database.



## MONITORING

A required field check is there in json schema check. If an attribute is missing from any row it will raise an error.

A wrong datatype check is present for every field in the json schema check.


### INCOMPLETE INSERTION DATA CHECK
A count check on the table present in database is done initially(before insertion) in the main module.

Again a count check is done after the insertion of the data.

Subtracting the initial count with the final count and checking its equality with the number of records in the input file.

The code will print the data is consistent if the count matches and will print data is inconsistent else wise.



## OTHER CHECKS THAT CAN BE MADE ON THIS PIPELINE

Check for the duplicate records.

Check for date and timestamp formats instead of string check.

A suspense table can be maintained to keep monitoring the failed_records, incomplete_records, last_load_datetime of the pipeline and the same table can be updated after every run.

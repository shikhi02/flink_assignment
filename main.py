from validator import *
from mysql_connector import *


file_name = '/Users/shikharrauthan/Downloads/202110_flink_data_engieering_sample_data.json'

insert_query = "INSERT INTO table_name(event_type, event_time, data, processing_date) VALUES ({}, {}, {}, {})".format(event_type, event_time, data, processing_date)

count_query = "SELECT COUNT(1) as count_rows FROM table_name"

def main(file_name=file_name):
    """
    note: pipeline is working and executable till step-3.
    need to attach a mysql db by providing credentials in .db_config_flink file to make it runnable after that.

    step-0 Checking count before insertion of the data in the table.

    step-1 Read json file and take a json dump(list of nested dictionaries). 
    For now the file name is used as a global variable which can be replaced by any input file.

    step-2 Variables are defined for processing file in batches to handle a big input file.
    These values can be altered according to use-case.

    step-3 Validation in batches of 5000 events to handle big data file.

    step-4 Insertion in mysql database through an insertion script.

    step-5 Checking count in db and file after every run. To confirm the data consistency.
    """

    # step-0 Checking count before insertion
    count_before = mysql_conn_obj.fetch(count_query, ['count_rows'])[0]

    # step-1 Reading from file
    with open(file_name, 'r') as f:
        list_events = [json.loads(line) for line in f]

    data = json.loads(json.dumps(list_events))

    # step-2 defining variables for batches
    len_data = len(data)
    event_start = 0
    event_end = 5000

    # step-3 validating data of the json file
    while len_data >= event_start+1:
        print(event_start, event_end)
        for i in data[event_start:event_end]:
            is_valid, msg = validate_json(i)
            if is_valid:
                # step-4 insert each valid element in mysql db
                mysql_conn_obj.execute_script(insert_query).format(i['event_type'],i['event_time'],i['data'],i['processing_date'])

        event_start = event_end+1
        if len_data < event_start + 5000:
            event_end = len_data
        else:
            event_end = event_start + 5000

    # step-5 checking data count with input file for consistency.
    
    count_after = mysql_conn_obj.fetch(count_query, ['count_rows'])[0]

    count_final_table = int(count_after) - int(count_before)

    if len_data == count_final_table:
        print("Data is consistent.")
    else:
        print("Data is inconsistent!")

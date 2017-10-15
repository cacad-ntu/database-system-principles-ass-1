"""
Execute all queries for questions
"""

import json
import time
import sys
from datetime import datetime

import prettytable
import psycopg2

# Parameter
HOST = "localhost"
DBNAME = "postgres_test"
USERNAME = "postgres"
PASSWORD = "admin"

def main(argv):
    """ main function to execute queries"""   
    if len(argv) == 1:
        print("ErrorNotEnoughArgument: Please input SQL file path!")
        return

    with open(argv[1], "r") as query_file:
        query_str = query_file.read()

    conn_string = "host='%s' dbname='%s' user='%s' password='%s'"%(HOST, DBNAME, USERNAME, PASSWORD)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    start_time = time.time()
    cursor.execute(query_str)
    exec_time = time.time() - start_time

    print("Execute: ", argv[1])
    print("Time elapsed: ", exec_time)
    
    res = cursor.fetchall()
    result_file_name = datetime.now().strftime("result_%Y_%m_%d_%H_%M_%S.json")
    with open("results/"+result_file_name, "w") as res_file:
        json.dump(res, res_file)
    
    res_tables = prettytable.PrettyTable()
    for item in res:
        res_tables.add_row(item)
    print(res_tables)
    
if __name__ == '__main__':
    main(sys.argv)


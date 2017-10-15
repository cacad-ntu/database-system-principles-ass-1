"""
Start script that will parse xml file and store it in postgres sql
"""

import logging
import json
import sys

from xml_parser.parser import parse_file
from tag_processor.processor import process_tag
from db_writer.db_client import DBClient

def init_logger(log_file):
    """ Initialise logger """
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s][%(message)s]'
    )

def main(argv):
    """ Main function to parse xml file """
    if len(argv) == 1:
        print("ErrorNotEnoughArgument: Please input config file path!")
        return

    with open(argv[1], "r") as conf_file:
        conf = json.load(conf_file)
    
    init_logger(conf["log"]["log_path"])
    logging.info("Start processing")

    db_conf = conf["db"]
    db = DBClient(db_conf["host"], db_conf["database"], db_conf["username"], db_conf["password"])

    count = 0
    pub_count = 0
    err_count = 0
    xml_conf = conf["xml"]
    skip_mod = xml_conf["skip_mod"]
    for tag in parse_file(xml_conf["xml_path"], xml_conf["header_line"], xml_conf["root_tag"]):
        try:
            if count%skip_mod == 0:
                info = process_tag(tag)
                db.insert_pub(info)
                pub_count += 1
                if pub_count % 100 == 0:
                    print("Publication count: ", pub_count)
                    print("Error count: ", err_count)
                    logging.info("tag: %s", tag)
                           
            count += 1
            
                
        except Exception as e:
            err_count += 1
            logging.error("Error: %s, Tag: %s", e, tag)
            db.commit()

    logging.info("Finish processing")

if __name__ == '__main__':
    main(sys.argv)

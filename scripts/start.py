"""
Start script that will parse xml file and store it in csv
"""

import logging

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

def main():
    """ Main function to parse xml file """
    init_logger("data/parser.log")
    logging.info("Start processing")

    db = DBClient("localhost", "postgres", "postgres", "admin")

    count = 0
    err_count = 0
    for tag in parse_file("data/dblp.xml", 2, 'dblp'):
        try:
            info = process_tag(tag)
            db.insert_pub(info)
            count += 1
            if count % 100 == 0:
                print("Publication count: ", count)
                print("Error count: ", err_count)
                break
            # logging.info("tag: %s", tag)
        except Exception as e:
            err_count += 1
            logging.error("Error: %s, Tag: %s", e, tag)
            db.commit()
            if err_count%100 == 0:
                print("Err count: ", err_count)
                break

    logging.info("Finish processing")

if __name__ == '__main__':
    main()

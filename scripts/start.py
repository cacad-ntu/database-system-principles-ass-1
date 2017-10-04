"""
Start script that will parse xml file and store it in csv
"""

import logging

from xml_parser.parser import parse_file
from xml_parser.utils import get_tag

def init_logger(log_file):
    """ Initialise logger """
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s][%(message)s]'
    )

def main():
    """ Main function to parse xml file """
    init_logger("data/parser.log")
    logging.info("Start processing")

    for tag in parse_file("data/dblp.xml", 2, 'dblp'):
        test_process(tag)

    logging.debug("Finish processing")

def test_process(line):
    """ test """
    logging.debug("TAG:%s", get_tag(line))

if __name__ == '__main__':
    main()

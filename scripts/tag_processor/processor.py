"""
Process xml tag based on requirement
"""

import logging

from xml_parser import utils

def process_tag(tag):
    """ Process xml tag """
    logging.info("Processing tag %s", utils.get_tag(tag))

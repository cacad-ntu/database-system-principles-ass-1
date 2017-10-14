"""
Process xml tag based on requirement
"""

import logging

import xml.etree.ElementTree as ET
from xml_parser import utils
from tag_processor.entity import ENTITY

def process_tag(tag):
    """ Process xml tag """
    logging.info("Processing tag %s", utils.get_tag(tag))
    header = ENTITY.format(utils.get_tag(tag))
    tag_root = ET.fromstring(header + tag)

    entry = get_publication_info(tag_root)
    return entry

def get_publication_info(tag_root):
    """ Get publication information from xml tag """
    info = {}

    info['pub_class'] = tag_root.tag
    info['pub_key'] = tag_root.get('key')

    key_info = info['pub_key'].split('/')
    info['pub_type'] = key_info[0]
    info['title_abbrev'] = key_info[1]

    info['authors'] = []

    for child in tag_root:
        if child.tag == 'author' or child.tag == 'editor' :
            info['authors'].append(child.text)
        else:
            info[child.tag] = child.text

    mdate = tag_root.get('mdate').split('-')

    if 'year' not in info:
        info['year'] = mdate[0]

    info['month'] = mdate[1]

    return info

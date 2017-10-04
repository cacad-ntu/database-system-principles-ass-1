"""
Parse xml file line by line
"""

import logging

from xml_parser import utils

def parse_file(file_path, header_line_count, root):
    """
    Parse file per tag and send it to tag_processor
    file_path -- path to file
    header_line_count -- header line that need to be skipped
    root -- root tag
    """
    logging.info("Parsing file %s", file_path)

    with open(file_path, 'r') as input_file:
        cur_tag = ""
        tag_buffer = ""

        for line in input_file:
            if header_line_count > 0:
                header_line_count -= 1
                continue

            if line[-1] == '\n':
                line = line[:-1]

            if line == utils.get_closing(root):
                break

            if cur_tag == "":
                cur_tag = utils.get_tag(line)
                if cur_tag == root:
                    cur_tag = ""
                    continue

            tag_buffer += line

            if line == utils.get_closing(cur_tag):
                yield tag_buffer
                cur_tag = ""
                tag_buffer = ""

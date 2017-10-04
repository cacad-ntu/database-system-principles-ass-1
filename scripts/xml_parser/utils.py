"""
Contain utility function for parsing xml file
"""

def get_tag(line):
    """ get xml tag from line """
    tag = line.split(' ')[0][1:]
    if tag[-1] == '>':
        tag = tag[:-1]
    return tag

def get_closing(tag):
    """ get closing string of a tag """
    return '</' + tag + '>'

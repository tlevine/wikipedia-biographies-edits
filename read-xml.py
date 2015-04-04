#!/usr/bin/env python3
import re
from collections import OrderedDict

import lxml.etree

fn = '/lockers/tlevine_vol/jail/big.dada.pink/wikipedia-dumps/enwiki-20150304-pages-meta-history1.xml-p000009967p000010000'

REVERT = re.compile(r'revert', flags = re.IGNORECASE)

def main():
    import sys
    for table_name, row in parse(fn):
        if table_name == 'revision':
            if re.match(REVERT, row['comment']):
                sys.stdout.write(row['comment'] + '\n')

def _field(element, name):
    ns = {'w': 'http://www.mediawiki.org/xml/export-0.10/'}
    elements = element.xpath('child::w:' + name, namespaces = ns)
    if len(elements) == 1:
        return str(elements[0].xpath('string()')).strip()
    elif len(elements) > 1:
        raise AssertionError('Multiple %s elements' % name)
    else:
        return ''

def parse(fn):
    xml = lxml.etree.iterparse(fn)
    for end, page_element in xml:
        if page_element.tag.endswith('page'):
            print(end)
            page_id = page_element[2].text
            yield 'page', {
                'title': page_element[0].text,
                'ns': page_element[1].text,
                'id': page_id,
            }
            for revision_element in page_element.iterchildren():
                if revision_element.tag.endswith('revision'):
                    names = ['id', 'timestamp', 'contributor', 'comment']
                    x = {name: _field(revision_element, name) for name in names}
                    x['page_id'] = page_id
                    yield 'revision', x

if __name__ == '__main__':
    main()

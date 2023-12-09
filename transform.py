#!/usr/bin/env python3

import sys
import json
import xml.etree.ElementTree as ET


def read_tuya_xml(file):
    with open(file) as f:
        root = ET.parse(f)
        for elt in root.iter():
            if elt.tag == 'string' and elt.attrib['name'].startswith('s_home_data'):
                return elt.text.strip().replace('\\\\"', '"')


def map_tuya_to_k8sconf(data):
    for d in data:
        tuya_conf = {}
        tuya_conf['id'] = d['devId']
        tuya_conf['ip'] = ""
        tuya_conf['key'] = d['localKey']
        tuya_conf['name'] = ""
        tuya_conf['version'] = ""
        print(json.dumps(tuya_conf, indent=4), ',', sep='')


def main(args):
    content = read_tuya_xml('codes.xml')
    data = json.loads(content)
    # print(json.dumps(data, indent=2))
    map_tuya_to_k8sconf(data.get('deviceRespBeen'))


if __name__ == '__main__':
    main(sys.argv)

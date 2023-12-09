#!/usr/bin/env python3

import os
import xml.etree.ElementTree as ET


def main(args):
    with open('codes.xml') as f:
        content = ET.parse(f)

        print(content)


if __name__ == '__main__':
    main(os.argv)

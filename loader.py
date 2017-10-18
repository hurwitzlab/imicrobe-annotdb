#!/usr/bin/env python3
"""Load annots db"""

import argparse
import csv
import json
import os
import sqlite3
import sys

# --------------------------------------------------
def get_args():
    """get_args"""
    parser = argparse.ArgumentParser(description='Load annotsdb')
    parser.add_argument('file', metavar='file', help='Input file')
    parser.add_argument('-d', '--db', help='SQLite db name',
                        metavar='str', type=str, default='annots.db')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """start here"""
    args = get_args()
    infile = args.file
    db_name = args.db

    if not os.path.isfile(infile):
        print('"{}" is not a file.'.format(infile))
        sys.exit(1)

    if not os.path.isfile(db_name):
        print('"{}" does not exist.'.format(db_name))
        sys.exit(1)

    print('Will load "{}" -> "{}"'.format(infile, db_name))

    db = sqlite3.connect(db_name)
    insert = 'insert or replace into annot (sample_id, annots) values (?, ?)'

    with open(infile) as fh:
        reader = csv.DictReader(fh, delimiter='\t')

        for i, row in enumerate(reader):
            vals = dict([x for x in row.items() if x[1] != ''])

            if 'sample_id' in vals:
                sample_id = vals['sample_id']
                print('{:5}: {}'.format(i + 1, sample_id))

                db.execute(insert, (sample_id, json.dumps(vals)))

        print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()

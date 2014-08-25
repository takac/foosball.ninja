#!/usr/bin/env python
# encoding: utf-8

import argparse
from db.clean_db import clean
from foosball import app

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--clean-db', '-c', action='store_true',
                   dest='clean_db',
                   help='rerun database schema and load sample data')
args = parser.parse_args()
if args.clean_db:
    clean()
app.run(host='0.0.0.0', port=8080)

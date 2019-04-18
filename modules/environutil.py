import base64
import os
import re
from collections import OrderedDict
from datetime import date

from dateutil.relativedelta import relativedelta


def _type_env(rx_result):
    return os.getenv(rx_result.group('key'), '')


def _type_file(rx_result):
    with open(rx_result.group('file_path'), 'r') as f:
        data = f.read()
    return data


def _type_base64(rx_result):
    return base64.b64decode(rx_result.group('base64')).decode('utf-8')


def _type_date1(rx_result):
    groups = rx_result.groupdict()
    now = date.today()
    if groups['y'] or groups['m'] or groups['d']:
        y = int(groups['y']) if groups['y'] else 0
        m = int(groups['m']) if groups['m'] else 0
        d = int(groups['d']) if groups['d'] else 0
        if groups['op'] == '+':
            now += relativedelta(years=y, months=m, days=d)
        elif groups['op'] == '-':
            now -= relativedelta(years=y, months=m, days=d)
    return date.strftime(now, '%Y-%m-%d')


def _type_date2(rx_result):
    return rx_result.group('date')


_parsers = OrderedDict()
_parsers[_type_env] = re.compile(r'^env\((?P<key>[a-zA-Z]\w*)\)$')
_parsers[_type_file] = re.compile(r'^file\((?P<file_path>.+)\)$')
_parsers[_type_base64] = re.compile(r'^base64\((?P<base64>.+)\)$')
_parsers[_type_date1] = re.compile(r'^date\(now ?(?P<op>\+|-) ?((?P<y>[1-3])y)? ?((?P<m>[1-9]|1[01])m)? ?((?P<d>[1-9]|[1-5]\d)d)?\)$|^date\(now\)$')
_parsers[_type_date2] = re.compile(r'^date\((?P<date>20\d{2}-(?:0\d|1[0-2])-(?:3[01]|[12][0-9]|0[1-9]))\)$')
# Keep this entry at dict last position
_parsers[lambda x: x.group(0)] = re.compile(r'.+')


def substitute_env(data):
    rv = {}
    for k, v in data.items():
        for fn, rx in _parsers.items():
            result = rx.search(v.strip())
            if result:
                rv[k] = fn(result)
                break
    return rv

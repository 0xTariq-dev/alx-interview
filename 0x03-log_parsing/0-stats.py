#!/usr/bin/python3
"""Script that reads line by line from standard input and computes metrics"""

import re


def line_parser(line):
    """Parses a request log line and extracts data"""
    pt = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<code>\S+)',
        r'\s*(?P<size>\d+)'
    )
    statics = {
        'code': 0,
        'size': 0
    }
    line_fmt = f'{pt[0]}\\-{pt[1]}{pt[2]}{pt[3]}{pt[4]}\\s*'
    matching = re.fullmatch(line_fmt, line)
    if matching:
        statics['code'] = matching.group('code')
        statics['size'] = int(matching.group('size'))
    return statics


def print_statics(total_size, code_stats):
    """Print the calculated statics from the logs"""
    sorted_codes = {k: code_stats[k] for k in sorted(code_stats)}
    print(f'File size: {total_size}')
    [print(f'{k}: {v}', flush=True) for k, v in sorted_codes.items() if v > 0]


def update_statics(line, total_size, code_stats):
    """Updates the statics from the request Log"""
    line_statics = line_parser(line)
    code = line_statics.get('code', 0)
    if code in code_stats.keys():
        code_stats[code] += 1
    return total_size + line_statics['size']


def stats(*args, **kwargs):
    """Reads line by line from stdin and parses the line to extract metrics"""
    line_count = 0
    total_size = 0
    codes = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        while True:
            line = input()
            total_size = update_statics(line, total_size, codes)
            line_count += 1
            if line_count % 10 == 0:
                print_statics(total_size, codes)
    except (KeyboardInterrupt, EOFError):
        print_statics(total_size, codes)


if __name__ == '__main__':
    stats()

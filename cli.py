#!/usr/bin/env python3
"""Command-line interface for config-merge."""
import argparse
import json
import sys
from config_merge import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Deep-merge JSON configuration layers with last-layer precedence')
    parser.add_argument('path', help='Input data file')
    args = parser.parse_args(argv)
    with open(args.path, encoding='utf-8') as f:
        data = f.read()
    print(json.dumps(analyze(data), sort_keys=True))
    return 0

if __name__ == '__main__':
    sys.exit(main())

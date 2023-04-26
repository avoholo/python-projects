#!/usr/bin/env python3
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Program to Say Hello.')
    parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Give Name to Greet.')
    return parser.parse_args()
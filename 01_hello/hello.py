#! /usr/bin/env python3
"""
Author: Juan Arevalo <jp-27@outlook.com>
This is work done following the book Tiny Python Projects
    by Ken Youens-Clark <kyclark@gmail.com>
# Purpose: Say hello
"""


import argparse


#-------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()

#-------------------------------------------
def main():
    """Runs the program"""
    args = get_args()
    print('Hello, ' + args.name + '!')


#-------------------------------------------
if __name__ == '__main__':
    main()

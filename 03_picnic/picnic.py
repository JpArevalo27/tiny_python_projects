#!/usr/bin/env python3
"""
Author : Juan Arevalo <jp-27@outlook.com>
Date   : 2022-05-03
Purpose: Print a list of picnic items
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        nargs='+',
                        metavar='str',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default: False)',
                        action='store_true',
                        default = False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    start = "You are bringing "

    if args.sorted:
        items.sort()

    if len(items) == 1:
        print(start + items[0] + ".")
    elif len(items) == 2:
        print(start + items[0] + " and " + items[1] + ".")
    else:
        print(start, end='')
        for i in range(len(items) - 1):
            print(items[i] + ", ", end='')
        print("and " + items[-1] + ".")


       
   
  


# --------------------------------------------------
if __name__ == '__main__':
    main()

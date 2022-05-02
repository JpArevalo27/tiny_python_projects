#!/usr/bin/env python3
"""
Author : jparevalo <jparevalo@localhost>
Date   : 2022-04-27
Purpose: Test input processing
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='word',
                        help='A word')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run the program here"""

    args = get_args()
    word = args.positional
    print('Ahoy, Captain, a ' + word + ' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

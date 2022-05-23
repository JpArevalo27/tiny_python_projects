#!/usr/bin/env python3
"""
Author : juanarevalo <juanarevalo@localhost>
Date   : 2022-05-23
Purpose: Howler a message (upper-cases input)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename (default: )',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run the Howler Program"""

    args = get_args()
    
    # Copy input into a string we can handle
    input = ''
    if os.path.isfile(args.text):
        input = open(args.text).read()
    else:
        input = args.text

    # Here we determine if output needs to go to console or file and process it
    if not args.outfile: # If it goes to console, just print
        print(input.upper())
    else:                # If it goes to file, create and write or overwrite
        out_fh = open(args.outfile, 'wt')
        print(input.upper(), file=out_fh)
        out_fh.close()

    # The solution offered in the book replaces my last if with the following clever solution:
    #out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout # This requires the import of sys
    #out_fh.write(input.upper() + '\n')
    #out_fh.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()

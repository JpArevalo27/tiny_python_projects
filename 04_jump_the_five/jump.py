#!/usr/bin/env python3
"""
Author : juanarevalo <juanarevalo@localhost>
Date   : 2022-05-16
Purpose: Encrypt Messages
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')


    return parser.parse_args()

# --------------------------------------------------
def encryptMessage(sMessage):
    jumper = dict()
    jumper['1'] = '9'
    jumper['2'] = '8'
    jumper['3'] = '7'
    jumper['4'] = '6'
    jumper['5'] = '0'
    jumper['6'] = '4'
    jumper['7'] = '3'
    jumper['8'] = '2'
    jumper['9'] = '1'
    jumper['0'] = '5'

    output = ""
    for char in sMessage:
        output += jumper.get(char, char) # .get(char, return char if not in dict)

    return output


# --------------------------------------------------
def main():
    """Encrypt a message with this program"""

    args = get_args()
 
    print(encryptMessage(args.text))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

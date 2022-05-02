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

    parser.add_argument('word',
                        metavar='word',
                        help='A word')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run the program here"""

    args = get_args()
    word = args.word
    # ALL of this can be accomplished using str.format()

    #output = 'Ahoy, Captain, ' #first half of the output sentence before the article
    #char = word[0].lower()
    #if char in 'aeiou':
    #    output = output + 'an '
    #else:
    #    output = output + 'a '
    #output = output + word + ' off the larboard bow!'
    #print(output)

    
    # THIS IF can be simplified as
    #char = word[0].lower()
    #article = ''
    #if char in 'aeiou':
    #    article = 'an'
    #else:
    #    article = 'a'

    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))

    # ANOTHER WAY to simplify this is using f'string' like this
    #print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

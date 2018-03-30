#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from time import sleep


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--debug", action='store_true', default=False, help='Remote debug mode')
    args = parser.parse_args()

    if args.debug:
        import ptvsd
        print('waiting...')
        ptvsd.enable_attach('my_secret', address=('0.0.0.0', 3000))
        ptvsd.wait_for_attach()
        sleep(1)
        print('Debug Start')

    msg = 'hello'

    print(msg)


if __name__ == '__main__':
    main()

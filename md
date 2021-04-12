#!/usr/bin/env python3

import os
import sys

class Md(object):
    def __init__(self, args):
        self.dirs = args.dirs
        self.miles_time()


    def create_dirs(self):
        for dir in self.dirs:
            dirname = os.path.normpath(
                os.path.join(os.path.abspath(dir), self.time)
            )

            if not os.path.exists(dirname):
                print('Creating directory: {}'.format(dirname))
                try:
                    os.mkdir(dirname, 0o777)
                except IOError as e:
                    print('IOError: {}.'.format(e.args[1]))

    def miles_time(self):
        from datetime import datetime
        from math import ceil

        minute = int(datetime.now().strftime("%M"))
        minute = ceil(minute / 10) * 10
        minute = int(minute)
        now = datetime.now().strftime("%Y_%m_%d_%H")

        self.time = "%s%02d" % (now, minute)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('dirs', help='Locations where directories are created.', nargs='+', action='extend')

    md = Md(parser.parse_args())
    md.create_dirs()


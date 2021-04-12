from __future__ import print_function
import inspect
import sys


class Colour(object):
    def __init__(self):
        self.reset = '\033[0m'
        self.bold = '\033[1m'
        self.yellow = '\033[93m'
        self.red = '\033[91m'
        self.green = '\033[92m'
        self.blue = '\033[36m'
        self.underline = '\033[4m'


class Misc(object):
    def __init__(self):
        pass

    def ls(self, dir):
        import os
        import re

        if os.path.isdir(dir):
            items = []
            for item in os.listdir(dir):
                if not re.match('\.', item):
                    items.append(item)
        return items

    def miles_time(self):
        from datetime import datetime
        from math import ceil

        minute = int(datetime.now().strftime("%M"))
        minute = ceil(minute / 10) * 10
        minute = int(minute)
        now = datetime.now().strftime("%Y_%m_%d_%H")

        self.now = "%s%02d" % (now, minute)
        return self.now

    def miles_date(self):
        from datetime import datetime

        self.date = datetime.now().strftime("%Y_%m_%d")
        return self.date

    def mkdir(self, dirname):
        import os

        if not os.path.exists(dirname):
            try:
                os.mkdir(dirname, 0o777)
            except OSError as e:
                print("OS Error error({0}): {1}".format(e.errno, e.strerror))
                raise
            except IOError as e:
                print("I/O Error error({0}): {1}".format(e.errno, e.strerror))
                raise
            except:
                print('Unknown Error making directory: {}'.format(dirname))
                raise


class Print(object):

    def __init__(self):
        pass

    def success(self, string):
        d = ':'
        msg = string.split(d)
        print('{0}{1}{2}{3}{4}{5}'.format(
                                    Colour().green,
                                    Colour().bold,
                                    msg[0],
                                    Colour().reset,
                                    d,
                                    msg[1])
        )

    def warn(self, string):
        d = ':'
        msg = string.split(d)
        print('{0}{1}{2}{3}{4}{5}'.format(
                                    Colour().yellow,
                                    Colour().bold,
                                    msg[0],
                                    Colour().reset,
                                    d,
                                    msg[1])
        )

    def error(self, string):
        d = ':'
        msg = string.split(d)
        print('{0}{1}{2}{3}{4}{5}'.format(
                                    Colour().red,
                                    Colour().bold,
                                    msg[0],
                                    Colour().reset,
                                    d,
                                    msg[1])
        )

    def print_self(self):
        print('{0}{1}{2}{3}{4}'.format(
                                Colour().bold,
                                Colour().blue,
                                Colour().underline,
                                inspect.stack()[1][3],
                                Colour().reset)
        )



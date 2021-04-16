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
        self.p = Print()

    def ls(self, dir):
        import os
        import re
        print(dir)

        if os.path.isdir(dir):
            items = []
            for item in os.listdir(dir):
                if not item.startswith('.'):
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
            except (OSError, ValueError) as e:
                print(f'Error: {sys.exc_info()[0]}, os.mkdir({dirname}, 0o777) : {e.args}')
                info = sys.exc_info()[1]
                m.error(f'Error: {info}')
                print(f'\tos.mkdir(\n\t\t{d}, 0o777)')
                return
            except:
                print('Unknown Error making directory: {}'.format(dirname))
                raise

    def find_common(self, item_list, **kwargs):
        import re
        from difflib import SequenceMatcher

        junk = False
        items = item_list
        inum = len(items)

        substring = None
        match = None
        for i in range(0, inum):
            for j in range(i+1, inum):
                s1 = items[i]
                s2 = items[j]

                if re.search(r'(\.\w?\.)', s1):
                    match = SequenceMatcher(lambda x : x == re.search(r'(\.\w?\.)', s1).group(0), s1, s2).find_longest_match(
                        0, len(s1),
                        0, len(s2)
                    )
                else:
                    print(s1)
                    match = SequenceMatcher(None, s1, s2).find_longest_match(
                        0, len(s1),
                        0, len(s2)
                    )

                substring = s1[match.a: match.a + match.size]

        self.p.success('Substring: {}'.format(substring), ':')

        return substring



class Print(object):

    def __init__(self):
        pass

    def success(self, string, *args):
        msg = string
        intro = ''
        delimeter = ''
        if len(args) > 0:
            delimeter = args[0]
            (intro, msg)= msg.split(delimeter)
            intro += Colour().reset


        print('{0}{1}{2}{3}{4}'.format(
                                    Colour().green,
                                    Colour().bold,
                                    intro,
                                    delimeter,
                                    msg)
        )

    def warn(self, string, *args):
        msg = string
        intro = ''
        delimeter = ''
        if len(args) > 0:
            delimeter = args[0]
            (intro, msg)= msg.split(delimeter)
            intro += Colour().reset

        print('{0}{1}{2}{3}{4}'.format(
                                    Colour().yellow,
                                    Colour().bold,
                                    intro,
                                    delimeter,
                                    msg)

        )

    def error(self, string, *args):
        msg = string
        intro = ''
        delimeter = ''
        if len(args) > 0:
            delimeter = args[0]
            intro= msg.split(delimeter)[0]
            msg= ':'.join(msg.split(delimeter)[1:])
            intro += Colour().reset

        print('{0}{1}{2}{3}{4}'.format(
                                    Colour().red,
                                    Colour().bold,
                                    intro,
                                    delimeter,
                                    msg)

        )


#!/usr/bin/env python3

import os
import argparse
import subprocess


class J(object):
    def __init__(self, args):
        self.args = args
        self.job_dir = os.getenv('JOB_DIR')
        self.postings = os.getenv('POSTINGS')

    def cd_job(self):
        cmd = f'open -a Terminal {self.job_dir}'
        subprocess.check_output(cmd.split())

    def cd_postings(self):
        cmd = f'open -a Terminal {self.postings}'
        subprocess.check_output(cmd.split())

    def ls_job(self):
        cmd = f'open -a Terminal {self.job_dir} ; /bin/ls -F'
        subprocess.check_output(cmd.split())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('project', help='Change directory to project..', action='store')
    #parser.add_argument('-j', help='Job to open shell in.', action='store_true')
    parser.add_argument('-p', '--postings', help='Version of flame to use.', action='store')
    parser.add_argument('-l', '--list', help='List Installed Versions.', action='store_true')
    args = parser.parse_args();

    j = J(args)
    j.cd_job()

    if (args.postings):
        j.cd_postings()
    elif (args.list):
        print('ls')
        j.ls_job



#!/bin/env python
"""
command-line driver for rogo client.
"""
import sys, cmd, json
from client import RogoClient


class RogoDriver(cmd.Cmd):
    prompt = ""
    completekey = ''
    cmdqueue = ''


    def __init__(self):
        self.client = RogoClient()

    def do_c(self, arg):
        """List challenges"""
        for x in self.client.list_challenges():
            print(json.dumps([x['id'], x['title']]))

    def do_q(self, arg):
        """Run the test suite."""
        return True

    def do_EOF(self, arg):
        """Exit"""
        return True


if __name__ == '__main__':
    RogoDriver().cmdloop()
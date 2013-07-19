#!/usr/bin/env python

from cmd2 import Cmd
from getpass import getuser
import sys
import requests

__version__ = '0.1'

class Application(Cmd):
 

    def __init__(self):
        Cmd.__init__(self)

    def do_greet(self,line):
        print "Hi! %s " %(getuser())

    def do_stock(self,line):
        link=requests.get('http://download.finance.yahoo.com/d/quote.csv?s='+line+'&f=l1')
        result=link.text
        print result

if __name__ == '__main__':
    app = Application()
    app.cmdloop()


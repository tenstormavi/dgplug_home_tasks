Myshell
=======

Assignment is to write a program that constitutes the following two commands:

1)greet : which will say "Hi" to the user.
2)stock : which will print the cureent stock value.

//These comands are to be executed using the requests library.

Code
====
::

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

Link
====

code is `here`_

.. _here: https://github.com/tenstormavi/dgplug_home_tasks/blob/master/myshell/shell.py

Run
====
::

$python shell.py

Output
======
::

        (virt1)[root@Avinash avinash]# python shell.py 
        (Cmd) greet
        Hi! avinash 
        (Cmd) stock GOOG
        910.68


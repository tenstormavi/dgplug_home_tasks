Sharevalue
==========
Our assignment is to print the latest share value of a company whose NASDAQ symbol would be given as command line argument.

Code
====
::
        #!/usr/bin/env python

        import urllib2 #<---------------------------------- the module is imported for opening url
        import sys     #<-----------------------------------sys module is imported for command line arguments

        def share(symbol): #<-------------The function is defined for opening and reading the url, and for printing sharevalue
        try:           #---------------Used for handle exception and error may be due to problems like url not opening
        link = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1') #<------opens the url
        r = float(link.read())  #<----------------------------------Reads the url
        if r == 0.00: #<---------------------if any wrong symbol is entered then it print the share
            print "The Nasdaq code entered is wrong"
        else:
            print "The current sharevalue for the given NASDAQ symbol is %f" % (r)
        except:
        print "failed to open the finance.yahoo.com url"

        if __name__ == '__main__':
        if len(sys.argv) !=2:
                print "Enter a valid NASDAQ symbol"
                sys.exit(1)
        else:
                share(sys.argv[1])
                sys.exit(1)

Link
====
Code is here: `sharevalue.py`_
.. _sharevalue.py:

Run
===
How to run the above command::
        $python sharevalue.py

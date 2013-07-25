Problem
=======
Assignment was to make a package which we can install in our system.It can find its dependency automatically and downlaod if necessary.

Download
========
The download the package `click here`_

.. _click here: https://testpypi.python.org/packages/source/s/shell_demo/shell_demo-0.4.tar.gz

Installation
=============
1. Extract the tar.gz
2. Go to that directory.
3. Then run this command in terminal: sudo python setup.py install

Run
===
::

$ shell_demo

Output
======
::
       
        (Cmd) (virt1)[root@Avinash shell_demo-0.4]# shell_demo 
        (Cmd) greet
        Hi! avinash
        (Cmd) hello Avinash
        Hello: Avinash
        (Cmd) stock GOOG
        Fetching recent share value of GOOG

        Current share price of company GOOG: 902.90

        (Cmd) stock FB
        Fetching recent share value of FB

        Current share price of company FB: 26.51

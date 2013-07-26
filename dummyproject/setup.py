#!/usr/bin/env python
"""avi_shell project"""

requirements = []

try:
    from setuptools import setup, find_packages
except ImportError:
    requirements.append('setuptools-0.9.7')

try:
    import requests
except ImportError:
    requirements.append('requests')

try:
    from cmd2 import Cmd
except ImportError:
    requirements.append('cmd2')

setup(name = 'avi_shell',
    version = '1.0',
    description = "tenstormavi's shell",
    long_description = "A Test Module",
    platforms = ["Linux"],
    author = "tenstormavi",
    author_email = "avi.avinash3008@gmail.com",
    url = "https://github.com/tenstormavi",
    license = "MIT",
    packages = find_packages(),
    install_requires=requirements,
    scripts=['avi_shell'],
    data_files=[('/usr/bin',['avi_shell']),
    ('/usr/share/avi_shell', ['README.rst'])
    ]
    )

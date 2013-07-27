#!/usr/bin/env python
"""avi_shellv1 project"""
from setuptools import find_packages, setup

setup(name = 'avi_shellv1',
    version = '2.0',
    description = "tenstormavi's shell",
    long_description = "A Test Module",
    platforms = ["Linux"],
    author="Avinash Kumar Dasoundhi",
    author_email="avi.avinash3008@gmail.com",
    url="https://github.com/tenstormavi",
    license = "MIT",
    install_requires=[
        "setuptools",
        "requests",
        "cmd2",
        "pyparsing",
    ],
    dependency_links=[
        "https://pypi.python.org/packages/source/r/requests/requests-1.2.3.tar.gz",
        "https://pypi.python.org/pypi/cmd2/0.6.5.1#downloads",
        "https://pypi.python.org/pypi/pyparsing/1.5.7#downloads",
    ],
    include_package_data=True,
    packages=find_packages()
)

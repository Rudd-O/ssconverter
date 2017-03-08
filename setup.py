#!/usr/bin/env python2

import glob
from setuptools import setup
import os
import platform

dir = os.path.dirname(__file__)
version = "0.1.0"
path_to_readme = os.path.join(dir, "README.md")
readme = open(path_to_readme).read(-1)

classifiers = [
'Development Status :: 3 - Alpha',
'Environment :: X11 Applications :: GTK',
'Intended Audience :: End Users/Desktop',
'License :: OSI Approved :: GNU Lesser General Public License v2.1 or later (LGPLv2.1+)',
'Operating System :: POSIX :: Linux',
'Programming Language :: Python :: 3 :: Only',
'Programming Language :: Python :: 3.5',
'Topic :: Office/Business',
]

programs = [
    "ssconverter",
]

setup(
	name='ssconverter',
	version=version,
	description='A program to convert to CSV specific sheets of an OpenOffice / LibreOffice spreadsheet',
	long_description = readme,
	author='Manuel Amador (Rudd-O)',
	author_email='rudd-o@rudd-o.com',
	license="LGPLv2.1+",
	url='http://github.com/Rudd-O/ssconverter',
	package_dir=dict([
                    ("ssconverter", "src/ssconverter"),
					]),
	classifiers = classifiers,
	packages=["ssconverter"],
	scripts=["bin/%s" % p for p in programs],
	keywords="office libreoffice openoffice",
	requires=["pyuno"],
	zip_safe=False,
)

mm-CCCbackup
============

.. image:: https://img.shields.io/badge/version-1.0-blue.svg
		:target: https://github.com/mmartins000/mm-CCCbackup
		:alt: Latest Version

.. image:: https://img.shields.io/badge/build-passing-brightgreen.svg
		:alt: Build: passing

Written on Python 2.7.10.

This script backs up and restores Bombich CCC 4.x folder to/from a specified location.

Tested using Bombich CCC 4.1.13 (4496).

----

SUDO is required. Your user account must have been included in /etc/sudoers first. \
If you don't know how to do it, google 'Mac sudoers'.

System restart is required in case of import and remove.

usage: sudo python mm-CCCbackup.py 	[-h] [-r]
[-m IMPORTFOLDER | -x EXPORTFOLDER | -z [EXPORTZIP]]

optional arguments:
	-h, --help	show this help message and exit
	-r, --remove	removes CCC folder from its location
	-m IMPORTFOLDER, --importfolder IMPORTFOLDER
			imports from the selected source folder / zip file
	-x EXPORTFOLDER, --exportfolder EXPORTFOLDER
			exports to the selected destination folder
	-z EXPORTZIP, --exportzip EXPORTZIP
			exports to a specified zip file

EXPORTZIP is an optional argument. Defaults to cccbackup.zip on script folder.

import argparse
import os
import shutil
import zipfile
# -*- coding: utf-8 -*-
__author__ = 'marcelomartins'

# Marcelo Martins, linkedin.com/in/marcelomartins
# Version 1.0
# Written on Python 2.7.10
# This script backs up and restores Bombich CCC 4.x folder to/from a specified location.
# Tested using Bombich CCC 4.1.13 (4496)


def export(export_folder):
    try:
        ret = shutil.copytree(ccc_path, export_folder)
    except (IOError, os.error) as why:
        print why
        pass
        ret = 1
    else:
        print "\nCCC folders copied from " + ccc_root + " to " + export_folder + "\n"
    return ret


def export_remove(export_folder):
    try:
        ret = shutil.move(ccc_path, export_folder)
    except (IOError, os.error) as why:
        print why
        pass
        ret = 1
    else:
        print "\nCCC folders moved from " + ccc_root + " to " + os.pardir(export_folder)
        print_restart()
    return ret


def export_ziptree(export_folder, zip_filename):
    shutil.make_archive(zip_filename, "zip", export_folder)
    print "\nCCC folders zipped to " + zip_filename + ".zip\n"


def import_copy(import_folder):
    try:
        if zipfile.is_zipfile(import_folder):
            zf = zipfile.ZipFile(import_folder, 'r')
            zf.extractall(path=ccc_dir, members=None, pwd=None)
            zf.close()
            ret = shutil.move(ccc_dir, ccc_path)
        else:
            ret = shutil.copytree(import_folder + "/", ccc_path + "/")
    except (IOError, os.error) as why:
        print why
        pass
        ret = 1
    else:
        print "\nCCC folders imported to " + ccc_path
        print_restart()
    return ret


def main(ret=0):
    if args.exportfolder and not args.remove:               # Export (copy)
        ret = export(args.exportfolder)
    elif args.exportfolder and args.remove:                 # Export (move)
        ret = export_remove(export_folder_checked)
    elif args.exportzip:                                    # Export (zip)
        export_ziptree(ccc_path, args.exportzip)
    elif args.importfolder and not args.remove:             # Import
        ret = import_copy(args.importfolder)
    else:
        print parser.print_help()
    return ret


def print_restart():
    print "You must restart the system for changes to take effect.\n"


ccc_root = "/Library/Application Support/"
ccc_path = "/Library/Application Support/com.bombich.ccc"   # Hardcoded to avoids mistakes
ccc_dir = "com.bombich.ccc"

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--remove", help="removes CCC folder from its location", action="store_true")

group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-m", "--importfolder", action='store', help="imports from the selected source folder")
group1.add_argument("-x", "--exportfolder", action='store', help="exports to the selected destination folder")
group1.add_argument("-z", "--exportzip", help="exports to a specified zip file", action='store',
                    nargs='?', const='cccbackup')

args = parser.parse_args()

if args.remove:
    if not os.path.exists(args.exportfolder):
        export_folder_checked = os.pardir(args.exportfolder)
    else:
        export_folder_checked = args.exportfolder

if args.exportfolder and not os.path.exists(ccc_path):
    print "\nError: Could not find " + ccc_path + "\n"
    exit(1)

if args.exportzip and os.path.exists(args.exportzip):
    print "\nError: Zip file " + args.exportzip + " already exists.\n"
    exit(1)

if args.exportfolder and os.path.exists(args.exportfolder):
    print "\nError: Destination folder " + args.exportfolder + " already exists.\n"
    exit(1)

if args.importfolder and not os.path.exists(args.importfolder):
    print "\nError: Could not find source folder/file " + args.importfolder + "\n"
    exit(1)

if os.geteuid() == 0:
    main()
else:
    print "\nYou must be root or run this script with sudo." \
          "\nsudo: your user account must have been included in /etc/sudoers first." \
          "\nsudo: if you don't know how to do it, google 'Mac sudoers'." \
          "\nThen you can type: sudo python " + os.path.basename(__file__) + " [options]\n"
    exit(2)

# -*- coding:utf-8 -*-

import sys
import os
import shutil
from optparse import OptionParser



def check_argument(options, args):
	"""Check Argument
	"""
	if len(args) > 0:
		return False

	if not( options.input_dir and options.output_dir):
		return False

	return True


def fild_all_files(directory):
	"""Return full path of specific directory
	"""
	for root, dirs, files in os.walk(directory):
		yield root
		for file in files:
			yield os.path.join(root, file)


def main():
	""" Main Module
	"""
	# Add Option
	parser = OptionParser()
	parser.add_option(
		"-i","--input",
		action="store",
		type="string",
		dest="input_dir",
		help="Set Source Directory"
		)
	parser.add_option(
		"-o","--output",
		action="store",
		type="string",
		dest="output_dir",
		help="Set Destination Directory"
		)

	# Parse Argument
	(options, args) = parser.parse_args()

	# Check Argument
	if not check_argument(options, args):
		parser.error(u"ERROR\tInvalid Argument.")
		return -1

	# Get Argument
	input_dir  = options.input_dir
	output_dir = options.output_dir

	# Check directory path
	dirs = [ input_dir, output_dir ]
	for dir in dirs:		
		if not os.path.isdir(dir):
			print u"ERROR:\tDirectory is not exist. -> %s" % dir
			return -1

	# Copy files
	for file in fild_all_files(input_dir):
		# Get file extension
		root, ext = os.path.splitext(file)
		if ext != ".md":
			continue
		shutil.copy(file, output_dir)

	return 0


if __name__ == '__main__':
	sys.exit(main())

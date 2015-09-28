# -*- coding:utf-8 -*-

import sys
import os
import shutil
from optparse import OptionParser


def fild_all_files(directory):
	"""Return full path of specific directory"""
	for root, dirs, files in os.walk(directory):
		yield root
		for file in files:
			yield os.path.join(root, file)


if __name__ == '__main__':
	""" main """

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

	# コマンドラインの解析
	(options, args) = parser.parse_args()
	print options, args

	# コマンドライン引数のチェック
	if len(args) > 0:
		parser.error(u"ERROR\tInvalid Argument.")

	if not( options.input_dir and options.output_dir):
		parser.error(u"ERROR\tInvalid Argument.")

	# 引数取得
	input_dir = options.input_dir
	output_dir = options.input_dir

	# 引数チェック
	if not os.path.isdir(input_dir):
		print u"ERROR:\tDirectory is not exist. -> %s" % input_dir
		exit()
	if not os.path.isdir(output_dir):
		print u"ERROR:\tDirectory is not exist. -> %s" % output_dir
		exit()

	for file in fild_all_files(input_dir):
		# Get file extension
		root, ext = os.path.splitext(file)
		if ext != ".txt":
			continue
		shutil.copy(file, OUT_DIR)


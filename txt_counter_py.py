import glob
import os

def count_files(root_dir, ext):
	return sum(1 for _ in glob.iglob(root_dir + "**/*." + ext, recursive=True))


def for_each_file_in(root_dir, ext, action):
	for f in glob.iglob(root_dir + "**/*." + ext, recursive=True):
		action(f)


def count_lines_for_all(path, ext):
	line_count = 0

	def count_lines(filename, condition):
		with open(filename) as f:
			return sum(1 for line in f if condition(line))

	def non_empty_non_coment(line):
		return line.rstrip() and line[0] != "#"

	def line_sum(filename):
		nonlocal line_count
		line_count += count_lines(filename, non_empty_non_coment)

	for_each_file_in(path, ext, line_sum)
	return line_count


def count_characters_for_all(path, ext):
	char_count = 0
	def char_amount(filename):
		with open(filename) as f:
			return len(f.read())

	def char_sum(filename):
		nonlocal char_count
		char_count += char_amount(filename)

	for_each_file_in(path, ext, char_sum)
	return char_count

path = "D:\\data\\github\\bizzare\\production\\bizzare_v2\\src\\"

gd = "gd"
tscn = "tscn"

print("*.gd files: " + str(count_files(path, gd)))
print("*.tscn files: " + str(count_files(path, tscn)))

print("amount of lines in *.gd w/o comments&empty: " + str(count_lines_for_all(path, gd)))
print("amount of lines in *.tscn w/o comments&empty: " + str(count_lines_for_all(path, tscn)))

print("amount of chars in *.gd: " + str(count_characters_for_all(path, gd)))
print("amount of chars in *.tscn: " + str(count_characters_for_all(path, tscn)))

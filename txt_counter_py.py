import glob
import os

def count_files(root_dir, ext):
	return sum(1 for _ in glob.iglob(root_dir + "**/*." + ext, recursive=True))


def for_each_file_in(root_dir, ext, action):
	for f in glob.iglob(root_dir + "**/*." + ext, recursive=True):
		action(f)


def count_lines_for_all(path, ext):
	def count_lines(filename):
		with open(filename) as f:
			return sum(1 for line in f if line.rstrip() and line[0] != "#")
	
	line_count = 0
	def line_sum(filename):
		nonlocal line_count
		line_count += count_lines(filename)

	for_each_file_in(path, ext, line_sum)
	return line_count


def count_characters_for_all(path, ext):
	def count_chars(filename):
		with open(filename) as f:
			return len(f.read())

	char_count = 0
	def char_sum(filename):
		nonlocal char_count
		char_count += count_chars(filename)

	for_each_file_in(path, ext, char_sum)
	return char_count


def count_word_appearance_in_all(path, word):
	def count_word_in(filename):
		with open(filename) as f:
			#
			for line in f:
				if word in line:
					print(filename)
			#
			return sum(1 for line in f if word in line)

	word_count = 0
	def word_sum(filename):
		nonlocal word_count
		word_count += count_word_in(filename)

	for_each_file_in(path, "*", word_sum)
	return word_count

path = "D:\\data\\github\\bizzare\\production\\bizzare_v2\\src\\"
gd = "gd"
tscn = "tscn"

print("*.gd files: " + str(count_files(path, gd)))
print("*.tscn files: " + str(count_files(path, tscn)))

print("amount of lines in *.gd w/o comments&empty: " + str(count_lines_for_all(path, gd)))
print("amount of lines in *.tscn w/o comments&empty: " + str(count_lines_for_all(path, tscn)))

print("amount of chars in *.gd: " + str(count_characters_for_all(path, gd)))
print("amount of chars in *.tscn: " + str(count_characters_for_all(path, tscn)))

print("amount of dmg in *.gd: " + str(count_word_appearance_in_all(path, "dmg")))

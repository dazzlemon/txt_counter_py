import glob

def count_files(root_dir, ext):
	return sum(1 for _ in glob.iglob(root_dir + "**/*." + ext, recursive=True))


def count_for_all_in(path, ext, count_f):
	counter = 0
	for filename in glob.iglob(path + "**/*." + ext, recursive=True):
		with open(filename) as f:
			counter += count_f(f)
	return counter

def count_lines_for_all(path, ext):
	def count_lines(f):
		return sum(1 for line in f if line.rstrip() and line[0] != "#")
	return count_for_all_in(path, ext, count_lines)


def count_characters_for_all(path, ext):
	def count_chars(f):
		return len(f.read())
	return count_for_all_in(path, ext, count_chars)


def count_word_appearance_in_all(path, word):
	def count_word_in(f):
		#for line in f:
		#	if word in line:
		#		print(filename)
		return sum(1 for line in f if word in line)
	return count_for_all_in(path, "*", count_word_in)


path = "/media/dazzlemon/data/github/bizzare/production/bizzare_v2/src/"#"D:\\data\\github\\bizzare\\production\\bizzare_v2\\src\\"
gd = "gd"
tscn = "tscn"

print("*.gd files: " + str(count_files(path, gd)))
print("*.tscn files: " + str(count_files(path, tscn)))
print("amount of lines in *.gd w/o comments&empty: " + str(count_lines_for_all(path, gd)))
print("amount of lines in *.tscn w/o comments&empty: " + str(count_lines_for_all(path, tscn)))
print("amount of chars in *.gd: " + str(count_characters_for_all(path, gd)))
print("amount of chars in *.tscn: " + str(count_characters_for_all(path, tscn)))
print("amount of dmg in all: " + str(count_word_appearance_in_all(path, "dmg")))

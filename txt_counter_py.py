import glob

def count_files(root_dir, ext):
	return sum(1 for _ in glob.iglob(root_dir + "**/*." + ext, recursive=True))


def count_for_all_in(path, ext, count_f):
	counter = 0
	for filename in glob.iglob(path + "**/*." + ext, recursive=True):
		with open(filename) as f:
			counter += count_f(f)
	return counter


def count_for_all_lines(path, ext):
	return count_for_all_in(path, ext, lambda f: (sum(1 for line in f if line.rstrip() and line[0] != "#")))


def count_for_all_characters(path, ext):
	return count_for_all_in(path, ext, lambda f: (len(f.read())))


def count_for_all_word_appearance(path, word):
	return count_for_all_in(path, "*", lambda f: (sum((lambda _: 1)(print(f)) for line in f if word in line)))


path = "/media/dazzlemon/data/github/bizzare/production/bizzare_v2/src/"#"D:\\data\\github\\bizzare\\production\\bizzare_v2\\src\\"
gd = "gd"
tscn = "tscn"

print("*.gd files: " + str(count_files(path, gd)))
print("*.tscn files: " + str(count_files(path, tscn)))
print("amount of lines in *.gd w/o comments&empty: " + str(count_for_all_lines(path, gd)))
print("amount of lines in *.tscn w/o comments&empty: " + str(count_for_all_lines(path, tscn)))
print("amount of chars in *.gd: " + str(count_for_all_characters(path, gd)))
print("amount of chars in *.tscn: " + str(count_for_all_characters(path, tscn)))
print("amount of dmg in all: " + str(count_for_all_word_appearance(path, "dmg")))

import glob

count_for_all_in = lambda path, ext, count_f: (sum(([(count_f(f), f.close()) for f in [open(filename)]][0][0]) for filename in glob.iglob(path + "**/*." + ext, recursive=True)))
count_files = lambda root_dir, ext: (sum(1 for _ in glob.iglob(root_dir + "**/*." + ext, recursive=True)))
count_for_all_lines = lambda path, ext: (count_for_all_in(path, ext, lambda f: (sum(1 for line in f if line.rstrip() and line[0] != "#"))))
count_for_all_characters = lambda path, ext: (count_for_all_in(path, ext, lambda f: (len(f.read()))))
count_for_all_word_appearance = lambda path, word: (count_for_all_in(path, "*", lambda f: (sum((lambda _: 1)(print(f)) for line in f if word in line))))

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

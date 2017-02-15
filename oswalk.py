import os

tree = os.walk("tree")
for dirname, subdir, files in tree:
    # print(dirname)
    # print(subdir)
    print(files)

    for f in files:
        print(os.path.abspath(f))

os.system("touch sample.txt")


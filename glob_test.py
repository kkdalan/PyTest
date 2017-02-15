import glob, os.path

files = glob.glob("*.py")
for f in files:
    print(os.path.abspath(f))



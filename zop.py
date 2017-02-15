import os,sys

'''
fp = open("zop.txt","r")
zops = fp.readlines()
fp.close()
'''
if len(sys.argv) < 2:
    print("使用方法: python3 zop.py <filename>.txt")
    exit(1)

filename = sys.argv[1]
print(filename)

with open(filename,"r") as fp:
    zops = fp.readlines()

i = 1
os.system("clear")
print("The Zen of Python")
for zen in zops:
    print("Zen {:>2}: {}".format(i,zen),end="")
    i += 1




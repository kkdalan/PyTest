# -*- coding: utf-8 -*-

print "====[ 九九乘法表 ]===="
print
for i in range(2,10,4):
    for j in range(1,10):
        print "{}x{}={:>2}  ".format(i,j,i*j),
        print "{}x{}={:>2}  ".format(i+1,j,(i+1)*j),
        print "{}x{}={:>2}  ".format(i+2,j,(i+2)*j),
        print "{}x{}={:>2}  ".format(i+3,j,(i+3)*j)
    print

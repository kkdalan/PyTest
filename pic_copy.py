# -*- coding: utf-8 -*-

import os, shutil, glob
source_dir = "/Users/kkd/Downloads/"

disk = os.statvfs("/")

freespace = disk.f_bsize * disk.f_blocks

pngfiles = glob.glob(source_dir + "*.png")
jpgfiles = glob.glob(source_dir + "*.jpg")
giffiles = glob.glob(source_dir + "*.gif")
allfiles = pngfiles + jpgfiles + giffiles

allfilesize = 0
for f in allfiles:
    allfilesize += os.path.getsize(f)
    # print(f)

if allfilesize > freespace:
    print("磁碟空間不足")
    exit(1)

target_dir = source_dir + "output"
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)

os.mkdir(target_dir)
os.mkdir(target_dir + "/png")
os.mkdir(target_dir + "/jpg")
os.mkdir(target_dir + "/gif")
imageno = 1

print("開始複製檔案...")
for f in allfiles:
    filename = f.split('/')[-1]
    extname = filename.split('.')[-1]
    
    targetfile = target_dir + '/' + extname + '/' + str(imageno) + '.' + extname
    shutil.copyfile(f, targetfile)
    os.remove(f)
    print("已複製: " + targetfile)
    imageno += 1

print("複製完成!")

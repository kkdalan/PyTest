import urllib


def download_pic(file_no):
    url = "http://xxxxxxx/" + file_no + ".jpg"
    f = open(url.split("/")[-1],'wb')
    f.write(urllib.urlopen(url).read())
    f.close()

for no in range(1,185):
    file_no = ("0000" + str(no) )[-4:]
    download_pic(file_no)
    print( file_no + ".jpg has been downloaded!")

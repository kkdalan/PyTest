import os,json, datetime

with open("earthquake.json",'r') as fp:
    earthquakes = json.load(fp)

os.system("clear")
print("過去7天全球發生重大地震資訊: \n")
for eq in earthquakes['features']:
    print("地點: {}".format(eq['properties']['place']))
    print("震度: {}".format(eq['properties']['mag']))
    # earthquake date time
    et = float(eq['properties']['time'])/1000.0 
    d = datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H-%M-%S')
    print("時間: {}".format(d))
    print("-------------------------------------------------")

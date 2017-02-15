import sys,ast

if len(sys.argv) < 2:
    print("使用方法: python3 file_write.py <filename>.txt")
    exit(1)


no = 1
scores = dict()
while True:
    score = int(input("請輸入{}號的成績(-1:結束): ".format(no)))
    if score == -1: break
    scores[no] = score
    no += 1

with open(sys.argv[1],"w") as fp:
    fp.write(str(scores))

print("{}已儲存完畢".format(sys.argv[1]))

with open(sys.argv[1],"r") as fp2:
    score_data = fp2.read()
    scores = ast.literal_eval(score_data)
print("The following is the scores data in dictionary: ".format(sys.argv[1]))
print(scores)



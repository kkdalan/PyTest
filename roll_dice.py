import sys

def roll_dice(n):

    cnt = 0
    dice = [0,1,2,3,4,5,6]
    hub = []
    pick = []

    for x in dice:
        for i in range(1, n + 1):
            pick.append(x)
        hub.append(pick)
        pick = []
        print(str(hub))
    
    return cnt

if not (len(sys.argv) < 2 ):
    n = int(sys.argv[-1])
    count = roll_dice(n)
    print(str(count))




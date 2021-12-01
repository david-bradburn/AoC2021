
lastline = 1000
cnt = 0

with open("../misc/input.txt", "r") as f:
    for line in f:
        x = int(line)
        if(x > lastline):
            cnt += 1
        lastline = x

        print(int(line))
print(cnt)
##1722 expected
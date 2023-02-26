#
# read.py - Question 3b
#
fileobj = open('read.csv','r')
data = fileobj.readlines()
fileobj.close()

lines = []
genre = []
for line in data:
    splitline = line.strip().split(',')
    lines.append(splitline)

for i in range(len(lines)):
    genre.append(lines[i][1])

print(genre)

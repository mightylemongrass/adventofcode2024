fin = open('input.txt', 'r')

lines = [n.strip() for n in fin.readlines()]
lines = [n.split() for n in lines]

line1 = [int(n[0]) for n in lines]
line2 = [int(n[1]) for n in lines]
line1.sort()
line2.sort()

#p1

difference = 0
for n in range(0, len(line1)):
    difference += abs(line1[n]-line2[n])

print(difference)

#p2

difference2 = 0

for x in range(0, len(line1)):
    if line1[x] in line2:
        ind = line2.index(line1[x])
        count = 1
        while True:
            if line2[ind+1] == line1[x]:
                ind += 1
                count += 1
            else:
                break
        difference2 += count*line1[x]

print(difference2)
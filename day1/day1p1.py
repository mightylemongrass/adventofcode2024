fin = open('input.txt', 'r')


lines = [n.strip() for n in fin.readlines()]
lines = [n.split() for n in lines]

line1 = [int(n[0]) for n in lines]
line2 = [int(n[1]) for n in lines]
line1.sort()
line2.sort()

difference = 0
for n in range(0, len(line1)):
    difference += abs(line1[n]-line2[n])

print(difference)
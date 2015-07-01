N = int(raw_input())
A = [ int(x) for x in raw_input().split() ]
A.sort()
biger = A.pop()
while True:
	last = A.pop()
	if last < biger:
		break
print last
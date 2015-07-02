from collections import defaultdict
din = raw_input().split()
N = int(din[0])
M = int(din[1])

A = defaultdict(list)
B = []
for i in range(N):
	din = raw_input()
	A[din].append(i+1)

for i in range(M):
	din = raw_input()
	B.append(din)

for case in B:
	if A[case]:
		print " ".join([str(x) for x in A[case]]).strip()
	else:
		print -1
		
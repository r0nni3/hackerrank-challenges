N = int(raw_input())
L = []
for i in range(N):
	L.append([raw_input(),float(raw_input())])

second = sorted(list(set([grade for name,grade in L])))[1]
print '\n'.join([ name for name,grade in sorted(L) if grade == second ])
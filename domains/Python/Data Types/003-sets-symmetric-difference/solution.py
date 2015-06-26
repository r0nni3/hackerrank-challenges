M = int(raw_input())
m = set(raw_input().split())

N = int(raw_input())
n = set(raw_input().split())

a = list(m.difference(n).union(n.difference(m)))
for i in range(len(a)):
	a[i] = int(a[i])
a.sort()
for val in a:
	print val
n=int(raw_input())
l = []
for val in raw_input().split():
	l.append(int(val))
print(hash(tuple(l)))
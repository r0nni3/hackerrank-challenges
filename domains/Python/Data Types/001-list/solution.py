l = []
n = int(raw_input())
for i in range(n):
	raw = raw_input().split()
	if raw[0] == "append":
		l.append( int(raw[1]) )
	elif raw[0] == "insert":
		l.insert( int(raw[1]), int(raw[2]) )
	elif raw[0] == "remove":
		l.remove( int(raw[1]) )
	elif raw[0] == "pop":
		l.pop()
	elif raw[0] == "index":
		l.index( int(raw[1]) )
	elif raw[0] == "count":
		l.count( int(raw[1]) )
	elif raw[0] == "sort":
		l.sort()
	elif raw[0] == "reverse":
		l.reverse()
	elif raw[0] == "print":
		print l

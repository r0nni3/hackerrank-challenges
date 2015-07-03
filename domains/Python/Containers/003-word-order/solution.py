from collections import defaultdict
n = int(raw_input())
words = defaultdict(list)
count = [0 for i in range(n)]
for i in range(n):
	din = raw_input().strip()
	words[din].append(i)
	count[words[din][0]] += 1
print len( words )
print " ".join( [ str(x) for x in count if x != 0] )
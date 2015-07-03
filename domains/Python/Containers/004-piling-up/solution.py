def pile(n, sL):
	vpile = []
	first = True
	response = "Yes"
	while n-1 >= 0:
		if int(sL[0]) >= int(sL[n-1]):
			current = int(sL.pop(0))
		else: 
			current = int(sL.pop())
		if first:
			vpile.insert(0, current)
			first = False
		elif current <= vpile[0]:
			vpile.insert(0, current)
		else:
			response = "No"
			break
		n -= 1
	return response

T = int(raw_input())
for i in range(T):
	n = int(raw_input())
	sL = raw_input().split()
	print pile(n, sL)
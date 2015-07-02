text = raw_input()
s = raw_input()
x=0
count = 0
while(x<len(text)):
	x = text.find(s,x)
	if x != -1:
		count += 1
		x += len(s)-1
	else:
		break
print count
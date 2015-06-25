n = int(raw_input())
students = {}
avg = 0.0
for i in range(n):
	tmp = raw_input().split()
	students[tmp[0]] = tmp[1:]

search = raw_input()
for grade in students[search]:
	avg = avg + float(grade)

print "%.2f" % (avg/len(students[search]))
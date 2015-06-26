X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())

out = [ [x,y,z] for z in range(Z+1) for y in range(Y+1) for x in range(X+1) if x+y+z != N ]
out.sort()
print out
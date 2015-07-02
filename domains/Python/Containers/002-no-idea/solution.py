din = raw_input().split()
n,m = int(din[0]),int(din[1])
total = 0
N = raw_input().split()
A = set(raw_input().split())
B = set(raw_input().split())
total = sum([ 1 if x in A else -1 if x in B else 0 for x in N ])
print total
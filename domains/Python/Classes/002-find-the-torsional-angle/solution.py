from math import acos,sqrt,pi
class MyVector:
	def __init__(self, pa=[0,0,0], pb=[0,0,0]):
		self.value = (pb[0]-pa[0], pb[1]-pa[1], pb[2]-pa[2])

	def modulo(self):
		return sqrt(sum([ pow(x,2) for x in self.value ]))

	def dotProduct(self, vec):
		return sum([ self.value[x]*vec.value[x] for x in range(len(self.value)) ])

	def crossProduct(self, vec):
		#cx = self.value[1]*vec.value[2] - self.value[2]*vec.value[1]
		#cy = self.value[0]*vec.value[2] - self.value[2]*vec.value[0]
		#cz = self.value[0]*vec.value[1] - self.value[1]*vec.value[0]
		pa = [self.value[2]*vec.value[1], self.value[2]*vec.value[0], self.value[1]*vec.value[0]]
		pb = [self.value[1]*vec.value[2], self.value[0]*vec.value[2], self.value[0]*vec.value[1]]
		return MyVector(pa, pb)

A = [ float(x) for x in raw_input().split() ]
B = [ float(x) for x in raw_input().split() ]
C = [ float(x) for x in raw_input().split() ]
D = [ float(x) for x in raw_input().split() ]

AB = MyVector(A, B)
BC = MyVector(B, C)
CD = MyVector(C, D)

X = AB.crossProduct(BC)
Y = BC.crossProduct(CD)

PHI = (acos((X.dotProduct(Y))/(X.modulo() * Y.modulo())) * 180) / pi
print "%.2f" % (PHI)
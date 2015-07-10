from __future__ import division
from math import fabs,pow,sqrt

class MyComplex(complex):
	def __init__(self, cmpx):
		super(complex, cmpx)
		self.text = ""
		real = ""
		imag = ""

		if self.real != 0.0:
			real = "%.2f" % self.real
		if self.imag != 0.0:
			imag = "%.2f" % fabs(self.imag)

		if real == "" and imag == "":
			self.text = "0.00"
		elif  real != "" and imag == "":
			self.text += real
		elif  real == "" and imag != "":
			if self.imag < 0.0:
				self.text += "-"
			self.text += imag + "i"
		else:
			self.text += real
			if self.imag < 0.0:
				self.text += " - "
			else:
				self.text += " + "
			self.text += imag + "i"

	def __div__(self, other):
		try:
			x = (self.real*other.real + self.imag*other.imag) / (pow(other.real,2) + pow(other.imag,2))
			y = (self.imag*other.real - self.real*other.imag) / (pow(other.real,2) + pow(other.imag,2))
			return MyComplex(complex(x, y))
		except ZeroDivisionError:
			return MyComplex(complex(0, 0))

	def __truediv__(self, other):
		try:
			x = (self.real*other.real + self.imag*other.imag) / (pow(other.real,2) + pow(other.imag,2))
			y = (self.imag*other.real - self.real*other.imag) / (pow(other.real,2) + pow(other.imag,2))
			return MyComplex(complex(x, y))
		except ZeroDivisionError:
			return MyComplex(complex(0, 0))

	def __str__(self):
		return self.text

	def mod(self):
		return sqrt(pow(self.real,2) + pow(self.imag,2))


a = [ (float(x)) for x in raw_input().split() ]
b = [ (float(x)) for x in raw_input().split() ]
A = MyComplex(complex(a[0], a[1]))
B = MyComplex(complex(b[0], b[1]))

print str(MyComplex(A + B))
print str(MyComplex(A - B))
print str(MyComplex(A * B))
print str(MyComplex(A / B))
print "%.2f" % A.mod()
print "%.2f" % B.mod()
#!/bin/bash/env python

class Calculator:
	def __init__(self):
		pass

	def add(self ,x,y):
		return x+y
	
	def sub(self,x,y):
		return x-y

	def mul(self,x,y):
		return x*y


cal=Calculator()

print(cal.add(2,5))
print(cal.sub(5,1))
print(cal.mul(5,2))


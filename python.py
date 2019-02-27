import sys
import re

print(sys.version)

def sum_to(num):
	sum = 0
	for i in range(num + 1):
		sum += i
	return sum


def largest(arr):
	arr.sort()
	return arr[-1]


def occurances(str,letter):
	return str.lower().count(letter)
	#p = len(re.findall(f"{letter}", str,re.IGNORECASE))  #this is a slower way but still useful to learn regex
	#return p

def product(*args):
	product = 1
	for arg in args:
		product *= arg
	return product


print(sum_to(5))
print(largest([9,8,7,6,5,4,3,2,1,0]))
print(occurances("Moose","o"))
print(product(1,6,3,9,4))
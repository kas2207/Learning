def listnum(numberlist):
	theSum = 0
	for i in numberlist:
		theSum += i
	print theSum


L= []
for x in xrange(1,1000):
	if x % 3 == 0 or x % 5 == 0:
		L.append(x)
	else:
		next

if __name__ == '__main__':
	listnum(L)

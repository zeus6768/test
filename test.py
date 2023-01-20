def mR(n):
	if (n//1.25)%2 == 0:
		return n//1.25*1.25
	else:
		return (n//1.25+1)*1.25
	
while True:
	a = input()
	if a == "quit":
		break
	else:
		r = mR(float(a))
		print(r)
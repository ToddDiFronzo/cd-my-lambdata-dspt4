def enlarge(n):
	return n*100
	
print("HI")

if __name__ == "__main__":
	# only if run from the command line, do the following code:
	# otherwise dont
	print("JUNK")
	print("Global JUNK")
	
	y = float(input("Please input a number to enlarge: "))
	print(enlarge(y))
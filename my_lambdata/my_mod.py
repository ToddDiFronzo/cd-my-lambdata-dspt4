
# my_lambdata/my_mod.py

def enlarge(n):
	return n * 100


# don't do the below with other code, it messes up the script when you run so do what is after it
# print("Junk")
# print("Globabl Scope")

# y = float(input("Please input a number to enlarge: "))
# print(enlarge(y))


# do this instead
if __name__ == "__main__":
	# only if run from the command line, invoke the follwoing code
	# otherwise don't
	print("Junk")
	print("Globabl Scope")

	y = float(input("Please input a number to enlarge: "))
	print(enlarge(y))

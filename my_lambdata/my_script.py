import pandas

from cd-my-lambdata-dspt4.my_mod import enlarge

print("HI")

df = pandas.DataFrame({"x":[1,2,3], "y":[4,5,6]})
print(df.head())

x = 5
print("Enlarge", x, "TO"< enlarge(x))
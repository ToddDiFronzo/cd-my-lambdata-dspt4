pip install -i https://test.pypi.org/simple/ my-lambdata

# in future maybe:
# pip install my-lambdata

# Usage
from my_lambdata.my_mod1 import enlarge

x = 5
print("Enlarge", x, "TO", enlarge(x))

# or
# from my_lambdata import my_mod1
# 
# x = 5
# print("ENLARGE", x, "TO", my_mod1.enlarge(x))


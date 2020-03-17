pip install -i https://test.pypi.org/simple/ my-lambdata

# in future maybe:
# pip install my-lambdata

# Usage
from my_lambdata.my_mod1 import enlarge

x = 5
print("Enlarge", x, "TO", enlarge(x))
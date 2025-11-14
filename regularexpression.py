#Regular expressions (regex) in Python provide a powerful way to search, match, 
# and manipulate text based on specific patterns.

import re
txt = "I love eating chapati."
x =re.search(".I", txt, re.IGNORECASE)
print(x)

name ="My name is Rhodah"
y = re.sub("Rhodah", "Mulera", name)
print(y)
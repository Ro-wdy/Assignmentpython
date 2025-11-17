#Regular expressions (regex) in Python provide a powerful way to search, match, 
# and manipulate text based on specific patterns.
# also extract text patterns (emails, phone numbers,words etc.) from larger text bodies.


#(pattern, text to search)

import re
txt = "I love eating chapati."
#^, *, +, ?, {}, [], \, |, (), $, .
x =re.search("+i", txt)
print(x)

name ="My name is Rhodah"
y = re.sub("Rhodah", "Mulera", name)
print(y)

text = "Contact me at mulerarhodah@gmail.com"

# Pattern to find emails
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found.")
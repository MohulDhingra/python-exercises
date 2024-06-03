'''import re
data=['ramangel_123@yahoo.com','angelpriya@gmail.com','ram@gmail.com','shularavi@gmail.com']
for i in data:
    output=re.search(r"\D*gmail\D*",i)
    if output is not None:
        print(output)
'''
import re
data=['123','T123*','12*3*T','T123','@123']
for i in data:
    output=re.match(r"\w*\W+\w*",i)
    if output is not None:
        print(output)


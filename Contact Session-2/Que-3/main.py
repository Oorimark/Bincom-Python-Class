import os
import re

os.chdir(os.getcwd() + "\Que-3")

with open(r"baby2008 (1).html","r") as baby_file:
    read_baby_file = baby_file.read()
    # if search for <td></td>
    res = re.findall(r'<td>[A-Z]?[a-z]+</td>',read_baby_file)

baby_names = []
for i in res:
    baby_names.append(i[4: len(i) - 5])

print(baby_names)

# print individual names
# for i in baby_names:
#     print(i)
import os

a = []

for i in range(65, 91):
    if os.path.exists(f"{chr(i)}:"):
        a += [chr(i)]

g = []

for i in a:
    for r, l, h in os.walk("E:"):
        g += [[r]+["\\"]+h]

x = ""
user = input("Enter path: ")

for i in g:
    for j in i:
        x += f"{j}"
    if user in x[-len(user)-1:]:
        print(x)
    x = ""
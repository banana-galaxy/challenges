from sys import argv
import os

if len(argv) == 1:
    print("please specify a file to search for")
    quit()

files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

for f in files:
    if f"{argv[1].split('.')[0]}.py".lower() == f.lower():
        print("File exists")
        quit()

similar = []
for f in files:
    if argv[1].lower() in f.lower():
        similar.append(f)

almost = []
for f in files:
    count = 0
    if f not in similar:
        for i, char in enumerate(f):
            if i <= len(argv[1]) - 1:
                if char.lower() == argv[1][i].lower():
                    count += 1
        if count > 0:
            almost.append([count, f])
almost = sorted(almost, reverse=True)

if similar:
    print("File not found however here are similar ones:")
    for i in similar:
        print(i)
    for i in almost:
        print(i[1])
        if i[0] == 1:
            break
else:
    user = input("File not found, would you like to create it? [Y/n] ")
    if user.lower() == "y" or user == '':
        newf = f"{argv[1].split('.')[0]}.py"
        with open(newf, 'w') as f:
            f.write('')
        print(f"file {newf} created")

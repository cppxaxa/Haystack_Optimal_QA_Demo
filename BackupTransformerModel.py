

import os
import sys

if len(sys.argv) <= 1:
    print("Syntax", sys.argv[0], "{keyword}")
    exit()

path = "/home/ubuntu/.cache/torch/transformers"

jsonFiles = [os.path.join(path, el) for el in os.listdir(path) if os.path.splitext(el)[1] == ".json"]

idToDelete = []

for fname in jsonFiles:
    data = None
    with open(fname) as f:
        data = f.read()

    if data.find(sys.argv[1]) >= 0:
        print(fname, data)
        print()

        idToDelete.append(os.path.splitext(fname)[0] + "")

print("\n\n")
print(idToDelete)

for el in idToDelete:
    if os.path.exists(el):
        print("True")
    else:
        print("False")

dest = "./cache_backup"
with open(sys.argv[1].replace('/', '_') + "_make_backup.sh", "w") as f:
    for el in idToDelete:
        f.write("mv {source} {dest}/.".replace("{source}", el + ".lock").replace("{dest}", dest) + "\n")
        f.write("mv {source} {dest}/.".replace("{source}", el + ".json").replace("{dest}", dest) + "\n")
        f.write("mv {source} {dest}/.".replace("{source}", el).replace("{dest}", dest) + "\n")

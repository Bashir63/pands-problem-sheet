import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    data = f.read()
    Es = data.count("e")

print(Es)    


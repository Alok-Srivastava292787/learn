from copy import copy, deepcopy
a=[4,6,[7,8]]
b=copy(a)

print(f"shallow copy \na={a}\nb={b}")

a.append(10)
#b=copy(a)
print(f"after appending source output of shallow copy \na={a}\nb={b}")

a[2].append(9)
#b=copy(a)
print(f"after adding nested list copy \na={a}\nb={b}")

b=deepcopy(a)
print(f"using deepcopy copy \na={a}\nb={b}")

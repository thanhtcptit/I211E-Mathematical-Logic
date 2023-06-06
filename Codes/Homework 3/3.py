# 1: Suzu is red
# 2: Suzu is green
# 3: Suzu is blue
# 4: Noto is red
# 5: Noto is green
# 6: Noto is blue
# 7: Wajima is red
# 8: Wajima is green
# 9: Wajima is blue
# 10: Anamizu is red
# 11: Anamizu is green
# 12: Anamizu is blue


def color_cnf(i):
    return [f"{i} {i + 1} {i + 2} 0", f"-{i} -{i + 1} 0", f"-{i} -{i + 2} 0", f"-{i + 1} -{i + 2} 0"]


def adjacent_cnf(i, j):
    return [f"-{i} -{j} 0", f"-{i + 1} -{j + 1} 0", f"-{i + 2} -{j + 2} 0"]


p = 12
cnfs = []
for c in [1, 4, 7, 10]:
    cnfs.extend(color_cnf(c))

for i, j in [(1, 4), (1, 7), (4, 7), (4, 10), (7, 10)]:
    cnfs.extend(adjacent_cnf(i, j))


with open("3.cnf", "w") as f:
    f.write(f"p cnf {p} {len(cnfs)}\n")
    f.write("\n".join(cnfs))

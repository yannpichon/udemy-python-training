from pathlib import Path

prenom_file = Path.cwd() / "prenom.txt"
prenom_sorted_file = Path.cwd() / "prenom_sorted.txt"
prenoms = []

with open(prenom_file) as f:
    content = f.read()
    for word in content.split():
        prenoms.append(word)

prenoms = [p.strip(" ,.") for p in prenoms]
prenoms.sort()

with open(prenom_sorted_file,"w") as f:
    f.write("\n".join(prenoms))
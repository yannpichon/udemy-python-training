from pathlib import Path

data_dir = Path.cwd() / "test"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for keys,values in d.items():
    for v in values:
        dir = data_dir / keys / v
        dir.mkdir(exist_ok=True, parents=True)
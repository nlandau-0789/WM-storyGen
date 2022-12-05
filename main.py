import random

seed = int(input("seed : "))
random.seed(seed)

noms_fem = [f"f{i}" for i in range(100)]
noms_hom = [f"m{i}" for i in range(100)]

actions = [f"a{i}" for i in range(10)]

role_fem = ["soeur", "mère", "femme", "tante", "pote"]
role_hom = ["frère", "père", "mari", "oncle", "pote"]

nb_fem = random.randint(0, 5)
nb_hom = random.randint(0, 5)

hom = random.choices(noms_hom, nb_hom)
fem = random.choices(noms_fem, nb_fem)

for i in range(random.randint(5, 10)):
    genre = random.choice(("homme", "femme"))
    if genre == "homme":
        print(f"{random.choice(hom)} est le {random.choice(role_hom)} de {random.choice(hom+fem)}")
    else :
        print(f"{random.choice(fem)} est la {random.choice(role_fem)} de {random.choice(hom+fem)}")

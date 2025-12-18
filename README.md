# chempkg

`chempkg` est un petit package Python permettant de manipuler des concepts chimiques simples :  
- Atomes (`Atom`)  
- Molécules (`Molecule`)  
- Analyse de réactions chimiques (`valid_reaction`)  
- Cinétique de décomposition (`kinetic_decomp`)

Ce projet est réalisé dans le cadre du module Python du Master.

## Structure du package


```bash
package_chimie/
├── chempkg/
│ ├── atom.py
│ ├── mol.py
│ ├── reaction_utils.py
│ └── __init__.py
└── tests
    ├── test_atom.py
    ├── test_molecule.py
    └── test_reactions_utils.py
└── README.md
└── pyproject.toml
```


## Prérequis

Le package utilise les bibliothèques suivantes :
- `numpy`
- `matplotlib`

Elles peuvent être installées avec :
```bash
pip install numpy matplotlib
```

## Fonctionnalités

### ● Classe `Atom`
Représente un atome avec :
- symbole
- masse atomique
- numéro atomique

Exemple :
```python
from chempkg.atom import Atom

carbon = Atom("C", 6, 12)
print(carbon)
# C (6, 12)

carbon.elec_config
# ('1s2', '2s2', '2p2')
```

### ● Classe `Molecule`
- Parse une formule chimique (`"H2O"`)
- Calcule la masse molaire
- Stocke les atomes sous forme d’un dictionnaire `{Atom: quantité}`

Exemple :
```python
from chempkg.mol import Molecule
from chempkg.atom import C, H, O

ethanol = Molecule("C2H5OH")

ethanol.weight
# 46.0

ethanol.atoms
# {C: 2, H: 6, O: 1}

ethanol.atoms.get(C)
# 2
```

### ● Fonction `valid_reaction(reactives, products)`
Détermine si une équation chimique est équilibrée.

Exemple :
```python
from chempkg.mol import Molecule
from chempkg.reaction_utils import valid_reaction

h2 = Molecule("H2")
o2 = Molecule("O2")
h2o = Molecule("H2O")

valid_reaction(
    reactives=[(h2, 2), (o2, 1)],
    products=[(h2o, 2)]
)
# True
```

### ● Fonction `kinetic_decomp(A0, k, T, steps, figure_path=None)`
Modélise une cinétique de décomposition exponentielle.

Exemple :
```python
from chempkg.reaction_utils import kinetic_decomp

A_t = kinetic_decomp(0.1, 0.5, 5, steps=10)
print(A_t)
```

## Installation

Prérequis : Python 3.10 - 3.12

1. Créer et activer un environnement virtuel (Windows)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
# ou
.venv\Scripts\activate.bat   # cmd.exe
```

2. Installer le package localement (mode développement)
```bash
pip install -e .
```
Ou installer depuis les sources (mode standard)
```bash
pip install .
```

3. Installer les dépendances de développement et lancer les tests
```bash
pip install pytest
pytest -q
```

4. Lancer l'exemple
Depuis le dossier `package_chimie` :
```bash
python run_example.py
```

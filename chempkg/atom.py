"""
Module atom

Ce module définit la classe Atom ainsi que les données associées aux éléments
chimiques utilisés dans le projet (liste des éléments, masses atomiques,
numéros atomiques et configurations électroniques).

Il fournit :
- la classe Atom pour représenter un atome chimique
- des constantes Atom pour les éléments de la biosphère considérée
- des structures de données utiles pour la construction des molécules
"""

# pylint: disable=invalid-name

class Atom:
    """
    Représente un atome chimique.

    Un atome est caractérisé par :
    - son symbole chimique (name),
    - son numéro atomique (nombre d'électrons),
    - sa masse atomique,
    - sa config électronique calculée selon la règle de Klechkowski.

    Les objets Atom sont immuables et hashables afin de pouvoir être utilisés
    comme clés dans des dictionnaires.
    """

    def __init__(self, name: str, num_electron: int, weight: float):
        self.name = name
        self.num_electron = num_electron
        self.weight = weight
        self.elec_config = Atom.get_orbitales(num_electron)

    @staticmethod
    def num_elec(l: int) -> int:
        """
        Calcule le nombre maximal d'électrons dans une orbitale de type l.

        Parametres : (l : int) Nombre quantique orbital (0=s, 1=p, 2=d, 3=f).

        Return : (int) Nombre maximal d'électrons dans l'orbitale.
        """
        return (2 * l + 1) * 2

    @staticmethod
    def get_orbitales(num_electron: int):
        """
        Calcule la configuration électronique d’un atome selon la règle de Klechkowski.

        Retourne un tuple de chaînes de caractères du type :
        ("1s2", "2s2", "2p4")
        """
        # Ordre de remplissage des orbitales (règle de Klechkowski)
        sorted_orbitales = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),
                            (4,1),(5,0),(4,2),(5,1),(6,0),(4,3),(5,2),
                            (6,1),(7,0),(5,3),(6,2),(7,1)]

        orbitales_letters = {0:"s", 1:"p", 2:"d", 3:"f"}

        config = []
        i = 0
        electrons_restants = num_electron

        while electrons_restants > 0:

            n, l = sorted_orbitales[i]
            capacite = Atom.num_elec(l)
            electrons = min(capacite, electrons_restants)
            electrons_restants -= electrons
            config.append(f"{n}{orbitales_letters[l]}{electrons}")

            i += 1

        return tuple(config)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"\n{self.name} ({self.num_electron}, {self.weight})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Atom):
            return (
                self.name == other.name
                and self.num_electron == other.num_electron
                and self.weight == other.weight
            )
        return False

# Données atomiques associées aux symboles chimiques :
atom_data = {
    "H": (1, 1),
    "C": (6, 12),
    "O": (8, 16),
    "N": (7, 14),
    "Ca": (20, 40),
    "P": (15, 31),
    "K": (19, 39),
    "S": (16, 32),
    "Na": (11, 23),
    "Cl": (17, 35.5),
    "Fe": (26, 56),
    "I": (53, 127),
    "F": (9, 19),
    "Co": (27, 59),
    "Mo": (42, 96)
}

# Instances Atom correspondant aux éléments chimiques utilisés.
# Ces objets sont partagés dans tout le projet.
H = Atom("H", 1, 1)
C = Atom("C", 6, 12)
O = Atom("O", 8, 16)
N = Atom("N", 7, 14)
Na = Atom("Na", 11, 23)
Cl = Atom("Cl", 17, 35.5)
F = Atom("F", 9, 19)
P = Atom("P", 15, 31)
S = Atom("S", 16, 32)
Ca = Atom("Ca", 20, 40)
K = Atom("K", 19, 39)
Fe = Atom("Fe", 26, 56)
I = Atom("I", 53, 127)
Co = Atom("Co", 27, 59)
Mo = Atom("Mo", 42, 96)

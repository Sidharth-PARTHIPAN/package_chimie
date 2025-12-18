"""
Module mol.

Ce module définit la classe Molecule, qui permet de représenter une molécule
chimique à partir de sa formule brute (ex: "H2O", "C6H12O6").

Il fournit les outils nécessaires pour :
- analyser une formule chimique sous forme de chaîne de caractères ;
- déterminer la composition atomique de la molécule ;
- calculer la masse molaire totale de la molécule.
"""

from chempkg.atom import H, C, O, N, Na, Cl, F, P, S, Ca, K, Fe, I, Co, Mo


# Dictionnaire associant un symbole chimique (str) à l'objet Atom correspondant.
# Il permet de convertir une formule chimique textuelle en objets Atom.
atom_data_lettre = {
    "H": H,
    "C": C,
    "O": O,
    "N": N,
    "Na": Na,
    "Cl": Cl,
    "F": F,
    "P": P,
    "S": S,
    "Ca": Ca,
    "K": K,
    "Fe": Fe,
    "I": I,
    "Co": Co,
    "Mo": Mo
}

class Molecule:
    """
    Représente une molécule chimique.

    Une molécule est définie par :
    - une formule chimique (ex: "C2H5OH") ;
    - un dictionnaire d'atomes indiquant la quantité de chaque atome ;
    - une masse molaire totale calculée à partir des masses atomiques.

    Les atomes sont stockés sous forme d'un dictionnaire :
        dict[Atom, int]
    où la clé est un objet Atom et la valeur le nombre d'atomes correspondants.
    """
    def __init__(self, formula : str):
        self.formula = formula

        # dict[Atom:int] (objets Atom comme clés, nombre d'atomes comme valeur)
        self.atoms = self.atoms_in_mol(formula)

        # float (masse totale de la molécule calculée à partir du poids des atomes qui la compose)
        self.weight = self.mol_weight()

    def atoms_in_mol(self, formula):
        """
        Analyse une formule chimique et extrait les atomes qui la composent.

        La formule est lue caractère par caractère afin d'identifier :
        - le symbole chimique (majuscule éventuellement suivie d'une minuscule) ;
        - le nombre d'atomes associé à ce symbole.

        Parametre : (formula : str) Formule chimique à analyser.

        Return : (dict[Atom, int]) Dictionnaire associant chaque atome au nombre de fois 
            où il apparaît dans la molécule.
        """

        atoms_dict = {}
        i = 0
        while i < len(formula):
            symbol = formula[i] # première lettre (majuscule)
            i += 1

            # Si la lettre suivante est en minuscule alors elle fait partie de l'atome
            if i < len(formula) and formula[i].islower():
                symbol += formula[i]
                i += 1

            # Lire le nombre qui suit le symbol s'il existe
            number_str = ""
            while i < len(formula) and formula[i].isdigit():
                number_str += formula[i]
                i += 1

            # Si il n'y a pas de nombre qui suit mettre 1 par défaut
            count = int(number_str) if number_str else 1

            # Verifier que le symbole est présent dans la biosphere qu'on s'est donné
            if symbol not in atom_data_lettre:
                raise ValueError(f"Ce symbole n'appartient pas au biosphère donné: {symbol}")

            atom_lettre = atom_data_lettre[symbol] # conversion symbole en instance Atom

            # On ajoute si le symbole était déjà présent sinon in initialise à 0 et on ajoute
            atoms_dict[atom_lettre] = atoms_dict.get(atom_lettre, 0) + count

        return atoms_dict

    def mol_weight(self):
        """
        Calcule la masse molaire totale de la molécule.

        La masse est obtenue en sommant, pour chaque atome,
        le produit de sa masse atomique par son nombre d'occurrences.

        Return : (float) Masse molaire de la molécule.
        """
        poids = 0
        for key, values in self.atoms.items():
            poids += key.weight * values # key.weight provient de l'objet Atom
        return float(poids)

    def __repr__(self):
        return f"Molecule({self.formula})"

    def __str__(self):
        return self.formula

    def __eq__(self, other):
        return isinstance(other, Molecule) and self.atoms == other.atoms

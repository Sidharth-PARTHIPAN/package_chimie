"""
Module reaction_utils.

Ce module contient des fonctions utilitaires liées aux réactions chimiques :
- vérification de la validité d'une réaction chimique (équilibrage des atomes) ;
- modélisation de la cinétique d'une réaction de décomposition du premier ordre.
"""

import numpy as np
import matplotlib.pyplot as plt


def valid_reaction(reactives, products):
    """
    Vérifie si une réaction chimique est valide (équilibrée).

    Une réaction est considérée comme valide si, pour chaque type d'atome,
    le nombre total d'atomes du côté des réactifs est égal au nombre total
    d'atomes du côté des produits.

    Parametres : reactives : list[tuple[Molecule, int]]
        Liste des réactifs sous la forme (molécule, coefficient stœchiométrique).
                 products : list[tuple[Molecule, int]]
        Liste des produits sous la forme (molécule, coefficient stœchiométrique).

    Return : bool, True si la réaction est équilibrée, False sinon.
    """

    dict_reac = {}
    dict_prod = {}

    for mol, coeff in reactives:
        for atom, count in mol.atoms.items():
            dict_reac[atom] = dict_reac.get(atom, 0) + coeff * count

    for mol, coeff in products:
        for atom, count in mol.atoms.items():
            dict_prod[atom] = dict_prod.get(atom, 0) + coeff * count

    return dict_reac == dict_prod

def kinetic_decomp(a0: float, k: float, t: float, steps: int = 10, figure_path: str = None):
    """
    Modélise la cinétique d'une réaction de décomposition du premier ordre.

    La concentration suit la loi :
        [A](t) = A0 * exp(-k * t)

    où :
    - A0 est la concentration initiale,
    - k est la constante de réaction,
    - t est le temps.

    Parametres : (a0 : float) Concentration initiale de la molécule.
                (k : float) Constante de vitesse de la réaction.
                (t : float) Temps total de la réaction.
                (steps : int) Nombre de points de temps calculés (par défaut 10).
                (figure_path : str or None) Chemin de sauvegarde de la figure. 
                    Si None, aucune figure n'est générée.

    Returns : numpy.ndarray
        Tableau contenant les concentrations [A](t) aux différents instants.
    """
    temps = np.linspace(0,t,steps)
    a_t = a0 * np.exp(-k*temps)
    if figure_path is not None:
        plt.figure(figsize = (6,6))
        plt.plot(temps, a_t)
        plt.xlabel("Temps en secondes")
        plt.ylabel("Concentration [A](t) en mol/L")
        plt.title("Evolution de [A](t)")
        plt.grid()
        plt.savefig(figure_path)
        plt.close()
    return a_t

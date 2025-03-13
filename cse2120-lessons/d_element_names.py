# d_element_names.py
"""
title: Chemical Element Names
author: Laksh Chopra
date-created 11/10/22
"""

ELEM_NAMES = {
    "H": "Hydrogen",
    "He": "Helium",
    "Na": "Sodium",
    "Cl": "Chlorine"
}

ELEM_ATOM_NUM = {
    "H": 1,
    "He": 2,
    "Na": 11,
    "Cl": 17
}

ELEM_MASS = {
    "H": 1.01,
    "He": 4.00,
    "Na": 22.99,
    "Cl": 35.45
}

if __name__ == "__main__":
    ELEMENT = "H"
    print(ELEM_NAMES[ELEMENT])
    print(ELEM_MASS["H"])
    print(ELEM_ATOM_NUM["H"])
    print(f"NACL's mass is {ELEM_MASS['Na'] + ELEM_MASS['Cl']} g/mol")


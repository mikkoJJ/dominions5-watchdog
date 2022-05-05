""" Helper methods and definitions for dealing with Dominions 5
game data.
"""

# The shortcut names for all nations:
NATIONS = {
    "Er": "Ermor",
    "Ul": "Ulm",
    "Mav": "Marverni",
    "Sa": "Sauromatia",
    "Ca": "Caelum",
    "Ct": "C'tis",
    "Ni": "Niefelheim",
    "Ka": "Kailasa",
    "Rl": "R'lyeh"
}

def get_nation_long_name(short_name: str) -> str:
    """ For a given shortened nation name, get the full
    name of that nation.

    Args:
        short_name (str): Dominions 5 nation short name used in logs

    Returns:
        str: the full name of that nation
    """
    return NATIONS[short_name]

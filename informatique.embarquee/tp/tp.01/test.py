"""
ENCODAGE:

A-type:

OP (8 bits), r1 (6 bits), r2 (6 bits), r3 (6 bits), padding (6 bits)

B-type:

OP (8 bits), r1 (6 bits), r2 (6 bits), aux (12 bits)
"""

# --- CONSTANTES ---

OPCODES = {
    """Dictionnaire des opcodes
    """
    "add": 0,
    "sub": 0,
    "mul": 0,
    "div": 0,
    "and": 0,
    "or": 0,
    "xor": 0,
    "addi": 0,
    "subi": 0,
    "muli": 0,
    "divi": 0,
    "andi": 0,
    "ori": 0,
    "xori": 0,
    "lw": 0,
    "sw": 0,
    "beq": 0,
    "bne": 0,
    "blo": 0,
    "bgt": 0,
}


# --- LECTURE DU FICHIER ---
def read_all_lines(path):
    """_summary_

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


# --- PARSING ---
def parse_line(line):
    """_summary_

    Args:
        line (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not line:
        raise ValueError("ligne vide")

    parts = line.split()
    mnemonic = parts[0]
    operands = " ".join(parts[1:]).split(
        ","
    )  # Séparation des opérandes par des virgules

    # Nettoyage de l'espace dans les opérandes
    operands = [op.strip() for op in operands]
    return mnemonic, operands


# --- TRADUCTION ---
def parse_register(reg_str):
    """Parse un registre

    Args:
        reg_str (string): registre au format $n

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not reg_str.startswith("$"):
        raise ValueError(f"registre invalide: {reg_str}")
    try:
        reg_num = int(reg_str[1:])
    except ValueError as exc:
        raise ValueError(f"registre invalide: {reg_str}") from exc

    if not 0 <= reg_num <= 63:
        raise ValueError(f"numéro de registre hors limites (0-63): {reg_num}")
    return reg_num


def parse_aux(aux_str):
    """Parse une valeur auxiliaire sur 12 bits.

    Args:
        aux_str (string): valeur auxiliaire

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    try:
        aux_val = int(aux_str)
    except ValueError as exc:
        raise ValueError(f"valeur auxiliaire invalide: {aux_str}") from exc
    if not -2048 <= aux_val <= 2047:  # FIXME Valeur signée sur 12 bits
        raise ValueError(f"valeur aux hors limites (-2048 à 2047): {aux_val}")
    return aux_val & 0xFFF  # FIXME On garde les 12 bits de poids faible


# Renvoie l'opcode correspondant au mnémonique
def get_opcode(mnemonic):
    """_summary_

    Args:
        mnemonic (_type_): _description_

    Raises:
        KeyError: _description_

    Returns:
        _type_: _description_
    """
    if mnemonic not in OPCODES:
        raise KeyError(f"mnemonic inconnu: {mnemonic}")
    return OPCODES.get(mnemonic)


def encodage_a(opcode, r1, r2, r3):
    """Encode une instruction de type A

    Args:
        opcode (_type_): l'opcode
        r1 (int): registre r1
        r2 (int): registre r2
        r3 (int): registre r3

    Returns:
        int: instruction encodée
    """
    instruction = (opcode << 24) | (r1 << 18) | (r2 << 12) | (r3 << 6) | 0
    return instruction


def encodage_b(opcode, r1, r2, aux):
    """Encode une instruction de type B

    Args:
        opcode (_type_): l'opcode
        r1 (int): registre r1
        r2 (int): registre r2
        aux (int): valeur auxiliaire sur 12 bits

    Returns:
        int: instruction encodée
    """
    instruction = (opcode << 24) | (r1 << 18) | (r2 << 12) | aux
    return instruction


def encode_instruction(mnemonic, operands):
    """Encode une instruction

    Args:
        mnemonic (_type_): mnémonique
        operands (list): liste des opérandes

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        int: instruction encodée
    """
    opcode = get_opcode(mnemonic)

    if mnemonic not in OPCODES:
        raise ValueError(f"mnemonic inconnu: {mnemonic}")

    if len(operands) != 3:
        raise ValueError(f"nombre d'opérandes invalide pour {mnemonic}")

    # Instructions de type A
    if mnemonic in ["add", "sub", "mul", "div", "and", "or", "xor"]:
        r1 = parse_register(operands[0])
        r2 = parse_register(operands[1])
        r3 = parse_register(operands[2])
        return encodage_a(opcode, r1, r2, r3)

    # Instructions de type B
    else:
        r1 = parse_register(operands[0])
        r2 = parse_register(operands[1])
        aux = parse_aux(operands[2])
        return encodage_b(opcode, r1, r2, aux)


# --- MAIN ---
SOURCE_PATH = "program.txt"
OUTPUT_PATH = "out.bin"
lines = read_all_lines(SOURCE_PATH)

# TEST: print(lines)
print("=== Lignes lues ===")
for li in lines:
    print(li)
print("===================")

for li in lines:
    m, o = parse_line(li)
    print(f"mnemonic: {m}, operands: {o}")

    opc = get_opcode(m)
    print(f"opcode: {opc}")
    print(f"opcode: {opc:#04x}")

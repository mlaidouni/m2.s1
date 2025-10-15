import sys
import re
import struct

# Opcode mapping
OPCODES = {
    "add": 1,
    "sub": 2,
    "mul": 3,
    "div": 4,
    "and": 5,
    "or": 6,
    "xor": 7,
    "addi": 8,
    "subi": 9,
    "muli": 10,
    "divi": 11,
    "andi": 12,
    "ori": 13,
    "xori": 14,
    "lw": 15,
    "sw": 16,
    "beq": 17,
    "bne": 18,
    "blo": 19,
    "bgt": 20,
}


def read_source(path):
    """Lit un fichier source et retourne une liste de lignes.

    Args:
        path (string): chemin du fichier source

    Returns:
        list of string: lignes du fichier.
    """
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def split_operands(operand_string):
    """Sépare les opérandes d'une instruction, par virgule.

    Args:
        operand_string (string): la chaîne des opérandes

    Returns:
        list of string: liste des opérandes
    """
    # On split par virgule, sans séparer les parenthèses et opérandes collées
    parts = [p.strip() for p in operand_string.split(",")]
    return [p for p in parts if p != ""]


def is_label(line):
    """Renvoie True si la ligne est un label (se termine par ':').

    Args:
        line (string): la ligne

    Returns:
        boolean: True si c'est un label, False sinon
    """
    return line.endswith(":")


# === Parsage des opérandes ===


def parse_register(s):
    """Parse un registre au format $n où n est entre 0 et 63.

    Args:
        s (string): la chaîne à parser

    Raises:
        ValueError: registre invalide
        ValueError: registre hors limites

    Returns:
        int: le numéro de registre
    """
    s = s.strip()
    if not s.startswith("$"):
        raise ValueError(f"registre invalide: {s}")
    n = int(s[1:])
    if not 0 <= n <= 63:
        raise ValueError(f"registre hors limites: {n}")
    return n


def parse_imm(s):
    """Parse une valeur immédiate.

    Args:
        s (string): la chaîne à parser

    Returns:
        int: la valeur immédiate.
    """
    return int(s.strip())


def parse_memory_operand(s):
    """_summary_

    Args:
        s (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    # "offset($base)", "($base)"
    s = s.strip()
    m = re.match(r"^([+-]?\d+)?\s*\(\s*(\$\d+)\s*\)$", s)
    if m:
        off = m.group(1)
        base = m.group(2)
        offset = int(off) if off is not None else 0
        return base, offset
    # Cas registre directe, e.g. "($0)"
    if s.startswith("(") and s.endswith(")"):
        inner = s[1:-1].strip()
        return inner, 0
    raise ValueError(f"format mémoire invalide: {s}")


# --- Encodage des instructions ---
def encodage_a(opcode, r1, r2, r3):
    """Encode une instruction de type A

    Args:
        opcode (int): l'opcode
        r1 (int): registre r1
        r2 (int): registre r2
        r3 (int): registre r3

    Returns:
        int: instruction encodée
    """
    return (opcode << 24) | (r1 << 18) | (r2 << 12) | (r3 << 6)


def encodage_b(opcode, r1, r2, aux):
    """Encode une instruction de type B (lw/sw, branchements, immediates)

    Args:
        opcode (int): l'opcode
        r1 (int): registre r1
        r2 (int): registre r2
        aux (int): valeur auxiliaire sur 12 bits

    Returns:
        int: instruction encodée
    """
    return (
        (opcode << 24) | (r1 << 18) | (r2 << 12) | (aux & 0xFFF)
    )  # 0xFFF pour garder 12 bits


def first_pass(lines):
    """Première passe: collecte des labels et des lignes d'instructions."""
    labels = {}
    instr_lines = []
    pc = 0
    for line in lines:
        if is_label(line):
            name = line[:-1].strip()
            if not name:
                raise ValueError("label vide")
            if name in labels:
                raise ValueError(f"label dupliqué: {name}")
            labels[name] = pc
        else:
            instr_lines.append(line)
            pc += 1
    return instr_lines, labels


def build_instr_atype(mnemonic, ops, opcode):
    """Construit une ligne de type A (3 registres).
    add/sub/mul/div/and/or/xor

    Args:
        mnemonic (string): mnemonic de l'opcode
        ops (string): opérandes
        opcode (int): opcode numérique

    Raises:
        ValueError: nombre d'opérandes incorrect

    Returns:
        int: instruction encodée
    """
    if len(ops) != 3:
        raise ValueError(f"{mnemonic} attend 3 opérandes")
    r1 = parse_register(ops[0])
    r2 = parse_register(ops[1])
    r3 = parse_register(ops[2])
    return encodage_a(opcode, r1, r2, r3)


def build_instr_btype_load_store(mnemonic, ops, opcode):
    """Construit une ligne de type B load/store (2 opérandes).

    Args:
        mnemonic (string): mnemonic de l'opcode
        ops (string): opérandes
        opcode (int): opcode numérique

    Raises:
        ValueError: nombre d'opérandes incorrect
        ValueError: offset hors plage

    Returns:
        int: instruction encodée
    """
    if len(ops) == 2:
        r1 = parse_register(ops[0])
        base_reg_str, offset = parse_memory_operand(ops[1])
        r2 = parse_register(base_reg_str)
        aux = offset
    else:
        raise ValueError(f"{mnemonic} attend 2 opérandes")
    if not -2048 <= aux <= 2047:
        raise ValueError(f"offset hors plage: {aux}")
    return encodage_b(opcode, r1, r2, aux)


def build_instr_btype_branch(mnemonic, ops, opcode, pc, labels):
    """Construit une ligne de type B branchement (3 opérandes).

    Args:
        mnemonic (string): mnemonic de l'opcode
        ops (string): opérandes
        opcode (int): opcode numérique
        pc (int): numéro de l'instruction courante
        labels (list of string): liste des labels connus

    Raises:
        ValueError: nombre d'opérandes incorrect
        KeyError: label inconnu
        ValueError: offset branch hors plage

    Returns:
        int: instruction encodée
    """
    if len(ops) != 3:
        raise ValueError(f"{mnemonic} attend 3 opérandes")
    r1 = parse_register(ops[0])
    r2 = parse_register(ops[1])
    target = ops[2]
    # si ce n'est pas un nombre (valeur immédiate), sinon on résout le label
    try:
        aux = parse_imm(target)
    except ValueError as exc:
        if target not in labels:
            raise KeyError(f"label inconnu: {target}") from exc
        label_pc = labels[target]
        # offset relatif (nombre d'instructions à sauter depuis l'instruction suivante)
        aux = label_pc - (pc + 1)
    if not -2048 <= aux <= 2047:
        raise ValueError(f"offset branch hors plage: {aux}")
    return encodage_b(opcode, r1, r2, aux & 0xFFF)


def build_instr_btype_immediate(mnemonic, ops, opcode):
    """Construit une ligne de type B immediate (3 opérandes).

    Args:
        mnemonic (string): mnemonic de l'opcode
        ops (string): opérandes
        opcode (int): opcode numérique

    Raises:
        ValueError: nombre d'opérandes incorrect
        ValueError: immédiate hors plage

    Returns:
        int: instruction encodée
    """
    if len(ops) != 3:
        raise ValueError(f"{mnemonic} attend 3 opérandes")
    r1 = parse_register(ops[0])
    r2 = parse_register(ops[1])
    aux = parse_imm(ops[2])
    if not -2048 <= aux <= 2047:
        raise ValueError(f"imm hors plage: {aux}")
    return encodage_b(opcode, r1, r2, aux & 0xFFF)


def assemble_line(line, pc, labels):
    """_summary_

    Args:
        line (_type_): _description_
        pc (_type_): _description_
        labels (_type_): _description_

    Raises:
        ValueError: _description_
        KeyError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        KeyError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """
    parts = line.split(None, 1)
    if not parts:
        raise ValueError("ligne vide")
    mnemonic = parts[0]
    operands_text = parts[1] if len(parts) > 1 else ""
    if mnemonic not in OPCODES:
        raise KeyError(f"mnemonic inconnu: {mnemonic}")
    opcode = OPCODES[mnemonic]

    ops = split_operands(operands_text)
    # Type A
    if mnemonic in ("add", "sub", "mul", "div", "and", "or", "xor"):
        return build_instr_atype(mnemonic, ops, opcode)

    # load/store: lw rd, offset(base)  OR  sw rs, offset(base)
    if mnemonic in ("lw", "sw"):
        return build_instr_btype_load_store(mnemonic, ops, opcode)

    # Branches: beq r1, r2, label
    if mnemonic in ("beq", "bne", "blo", "bgt"):
        return build_instr_btype_branch(mnemonic, ops, opcode, pc, labels)

    # immediates arithmétiques: addi r1, r2, imm
    if mnemonic.endswith("i"):
        return build_instr_btype_immediate(mnemonic, ops, opcode)

    raise NotImplementedError(f"format non géré pour {mnemonic}")


# === Assemblage finale ===
def assemble(src_path, out_path):
    """Assemble un fichier source en binaire.

    Args:
        src_path (string): chemin du fichier source
        out_path (string): chemin du fichier binaire de sortie
    """
    lines = read_source(src_path)
    instr_lines, labels = first_pass(lines)
    instructions = []
    for pc, line in enumerate(instr_lines):
        inst = assemble_line(line, pc, labels)
        instructions.append(inst)
    with open(out_path, "wb") as fout:
        for inst in instructions:
            fout.write(struct.pack(">I", inst))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python trad.py program.asm out.bin")
        sys.exit(1)
    assemble(sys.argv[1], sys.argv[2])

import sys
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

NB_REG = 64
MEM_SIZE = 4096

# Décodage inverse pour print debug
OPNAMES = {v: k for k, v in OPCODES.items()}


def sign_extend_12(x):
    """Convertit un entier 12 bits signé en entier Python.

    Args:
        x (int): entier 12 bits (0..4095)

    Returns:
        int: entier Python signé (-2048..2047)
    """
    if x & 0x800:
        return x - 0x1000
    return x


def extract_instructions_from_file(path):
    """Lit un fichier binaire et en extrait les instructions.

    Args:
        path (string): chemin du fichier binaire

    Returns:
        list of int: liste des instructions (entiers 32 bits)
    """
    with open(path, "rb") as f:
        data = f.read()

    # Chaque instruction est codée sur 4 octets (32 bits)
    # On lit le fichier par blocs de 4 octets
    instrs = [struct.unpack(">I", data[i : i + 4])[0] for i in range(0, len(data), 4)]
    return instrs


def run(path):
    """Exécute un programme binaire encodé par trad.py"""
    instrs = extract_instructions_from_file(path)

    reg = [0] * NB_REG
    mem = [0] * MEM_SIZE
    pc = 0

    # [DEBUG] Pour tester avec notre programme
    # mem[0] = 42  # Pour beq $1, $2 = true
    mem[0] = 7  # Pour beq $1, $2 = false

    while pc < len(instrs):
        current_instr = instrs[pc]
        # Décodage
        opcode = (current_instr >> 24) & 0xFF
        r1 = (current_instr >> 18) & 0x3F
        r2 = (current_instr >> 12) & 0x3F
        aux = sign_extend_12(current_instr & 0xFFF)

        # [DEBUG] Affichage de l'instruction décodée
        op_name = OPNAMES.get(opcode, f"INCONNU ({opcode})")
        print(f"[DEBUG] (PC={pc}) {op_name} r1={r1}, r2={r2}, aux={aux}")

        pc += 1  # on avance (conformément à ce qui est fait dans trad.py)

        # === Instructions de type A ===
        if opcode in (1, 2, 3, 4, 5, 6, 7):  # add/sub/mul/div/and/or/xor
            r3 = (current_instr >> 6) & 0x3F
            if opcode == 1:
                reg[r1] = reg[r2] + reg[r3]
            elif opcode == 2:
                reg[r1] = reg[r2] - reg[r3]
            elif opcode == 3:
                reg[r1] = reg[r2] * reg[r3]
            elif opcode == 4:
                reg[r1] = reg[r2] // reg[r3] if reg[r3] != 0 else 0
            elif opcode == 5:
                reg[r1] = reg[r2] & reg[r3]
            elif opcode == 6:
                reg[r1] = reg[r2] | reg[r3]
            elif opcode == 7:
                reg[r1] = reg[r2] ^ reg[r3]

        # === Instructions immédiates ===
        elif opcode in (8, 9, 10, 11, 12, 13, 14):  # addi/subi/muli/divi/andi/ori/xori
            if opcode == 8:
                reg[r1] = reg[r2] + aux
            elif opcode == 9:
                reg[r1] = reg[r2] - aux
            elif opcode == 10:
                reg[r1] = reg[r2] * aux
            elif opcode == 11:
                reg[r1] = reg[r2] // aux if aux != 0 else 0
            elif opcode == 12:
                reg[r1] = reg[r2] & aux
            elif opcode == 13:
                reg[r1] = reg[r2] | aux
            elif opcode == 14:
                reg[r1] = reg[r2] ^ aux

        # === Load / Store ===
        elif opcode == 15:  # lw
            addr = reg[r2] + aux
            if 0 <= addr < MEM_SIZE:
                reg[r1] = mem[addr]
            else:
                print(f"[ERROR] Adresse mémoire invalide: {addr}")

        elif opcode == 16:  # sw
            addr = reg[r2] + aux
            if 0 <= addr < MEM_SIZE:
                mem[addr] = reg[r1]
            else:
                print(f"[ERROR] Adresse mémoire invalide: {addr}")

        # === Branches ===
        elif opcode == 17:  # beq
            if reg[r1] == reg[r2]:
                pc += aux
        elif opcode == 18:  # bne
            if reg[r1] != reg[r2]:
                pc += aux
        elif opcode == 19:  # blo
            if reg[r1] < reg[r2]:
                pc += aux
        elif opcode == 20:  # bgt
            if reg[r1] > reg[r2]:
                pc += aux

        else:
            raise ValueError(f"Opcode inconnu: {opcode}")

        # Le registre $0 doit toujours rester à 0
        reg[0] = 0

    show_registers_memory_status(reg, mem)


def show_registers_memory_status(reg, mem):
    """Affiche le contenu des registres et de la mémoire après exécution."""
    print("=== Execution summurary ===")
    print("Registres (00–04):", reg[:4])
    print("Registres (05–09):", reg[5:9])
    print("Registres (10–14):", reg[10:14])
    print("Registres (15–19):", reg[15:19])
    print("Registres (20–24):", reg[20:24])
    print("Registres (25–29):", reg[25:29])
    print("Registres (30–34):", reg[30:34])
    print("Registres (35–39):", reg[35:39])
    print("Registres (40–44):", reg[40:44])
    print("Registres (45–49):", reg[45:49])
    print("Registres (50–54):", reg[50:54])
    print("Registres (55–59):", reg[55:59])
    print("Registres (60–63):", reg[60:63])
    print("Mémoire (00-10)  :", mem[:10])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python emulateur.py program.bin")
        sys.exit(1)
    run(sys.argv[1])

""" 
ENCODAGE:

A-type:

OP (8 bits), r1 (6 bits), r2 (6 bits), r3 (6 bits), padding (6 bits)

B-type:

OP (8 bits), r1 (6 bits), r2 (6 bits), aux (12 bits)
"""

OPCODES = {
	'addi': 0x08,
	'beq': 0x04,
	'xor': 0x26,
	'lw': 0x23,
	'sw': 0x2B,
}

source_path = "program.txt"
output_path = "out.bin"

# --------------------------------

# --- LECTURE DU FICHIER ---
def read_all_lines(path):
	with open(path, 'r', encoding='utf-8') as f:
		return [line.rstrip('\n') for line in f]

# --- PARSING ---
def parse_line(line):
	if not line:
		raise ValueError("ligne vide")

	parts = line.split()
	mnemonic = parts[0]
	operands = ' '.join(parts[1:]).split(',') # Séparation des opérandes par des virgules

	# Nettoyage de l'espace dans les opérandes
	operands = [op.strip() for op in operands]
	return mnemonic, operands

# --- TRADUCTION ---
def parse_register(reg_str):
	if not reg_str.startswith('$'):
		raise ValueError(f"registre invalide: {reg_str}")
	try:
		reg_num = int(reg_str[1:])
	except ValueError:
		raise ValueError(f"registre invalide: {reg_str}")
	if not (0 <= reg_num <= 63):
		raise ValueError(f"numéro de registre hors limites (0-63): {reg_num}")
	return reg_num

def parse_aux(aux_str):
	try:
		aux_val = int(aux_str)
	except ValueError:
		raise ValueError(f"valeur auxiliaire invalide: {aux_str}")
	if not (-2048 <= aux_val <= 2047):
		raise ValueError(f"valeur auxiliaire hors limites (-2048 à 2047): {aux_val}")
	return aux_val & 0xFFF  # On garde les 12 bits de poids faible

def 

# Renvoie l'opcode correspondant au mnémonique
def get_opcode(mnemonic):
	if mnemonic not in OPCODES:
		raise KeyError(f"mnemonic inconnu: {mnemonic}")
	return OPCODES.get(mnemonic)

# --- MAIN ---
lines = read_all_lines(source_path)

# TEST: print(lines)
print("=== Lignes lues ===")
for line in lines:
	print(line)
print("===================")

for line in lines:
	mnemonic, operands = parse_line(line)
	print(f"mnemonic: {mnemonic}, operands: {operands}")

	opcode = get_opcode(mnemonic)
	print(f"opcode: {opcode}")
	print(f"opcode: {opcode:#04x}")
# -------------------------
# Configuration du projet
# -------------------------

MCU = atmega328p
F_CPU = 16000000UL
BAUD = 115200

TARGET = authenticator

SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

CC = avr-gcc
OBJCOPY = avr-objcopy
CFLAGS = -Os -DF_CPU=$(F_CPU) -mmcu=$(MCU) -Wall -Wextra -std=c11

AVRDUDE = avrdude
PROGRAMMER = arduino
PORT = /dev/cu.usbmodem1301
BAUDRATE_UPLOAD = 115200


# -------------------------
# Règles
# -------------------------

all: $(TARGET).hex

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET).elf: $(OBJ)
	$(CC) $(CFLAGS) $^ -o $@

$(TARGET).hex: $(TARGET).elf
	$(OBJCOPY) -O ihex -R .eeprom $(TARGET).elf $(TARGET).hex
	@echo "Compilation terminée → $(TARGET).hex généré."

upload: $(TARGET).hex
	$(AVRDUDE) -c $(PROGRAMMER) -p $(MCU) -P $(PORT) -b $(BAUDRATE_UPLOAD) -D -U flash:w:$(TARGET).hex:i

clean:
	rm -f *.o *.elf *.hex

# -------------------------
# Affichage
# -------------------------

info:
	@echo "Sources : $(SRC)"
	@echo "Objets  : $(OBJ)"
	@echo "MCU     : $(MCU)"
	@echo "Port    : $(PORT)"
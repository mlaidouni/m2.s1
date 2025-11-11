WARNINGS := -Wall -Wextra -pedantic -Wshadow -Wpointer-arith -Wcast-align \
            -Wwrite-strings -Wmissing-prototypes -Wmissing-declarations \
            -Wredundant-decls -Wnested-externs -Winline -Wno-long-long \
            -Wstrict-prototypes -Wno-array-bounds

CFLAGS := -Os -DF_CPU=16000000UL -mmcu=atmega328p $(WARNINGS)

PORT := /dev/cu.usbmodem11201

# === Fichiers communs ===
COMMON := uart.c ring_buffer.c

# === Programme maître ===
master.elf: master.c $(COMMON)
	avr-gcc $(CFLAGS) -o $@ $^

master.hex: master.elf
	avr-objcopy -O ihex -R .eeprom $< $@

flash-master: master.hex
	avrdude -v -patmega328p -carduino -P$(PORT) -b115200 -D -Uflash:w:$<

# === Programme esclave ===
slave.elf: slave.c $(COMMON)
	avr-gcc $(CFLAGS) -o $@ $^

slave.hex: slave.elf
	avr-objcopy -O ihex -R .eeprom $< $@

flash-slave: slave.hex
	avrdude -v -patmega328p -carduino -P$(PORT) -b115200 -D -Uflash:w:$<

# === Nettoyage ===
clean:
	rm -f *.elf *.hex *.o
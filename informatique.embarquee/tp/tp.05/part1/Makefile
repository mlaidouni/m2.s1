WARNINGS := -Wall -Wextra -pedantic -Wshadow -Wpointer-arith -Wcast-align \
            -Wwrite-strings -Wmissing-prototypes -Wmissing-declarations \
            -Wredundant-decls -Wnested-externs -Winline -Wno-long-long \
            -Wstrict-prototypes -Wno-array-bounds

CFLAGS := -Os -DF_CPU=16000000UL -mmcu=atmega328p $(WARNINGS)

PORT := /dev/cu.usbmodem1301

upload: program.hex
	avrdude -v -patmega328p -carduino -P$(PORT) -b115200 -D -Uflash:w:$^

program.hex: program.elf
	avr-objcopy -O ihex $^ $@

program.elf: main.c buzzer.c
	avr-gcc $(CFLAGS) -o $@ $^

clean:
	rm -f *.elf *.hex *.o

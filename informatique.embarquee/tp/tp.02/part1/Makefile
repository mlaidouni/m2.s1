PORT := /dev/cu.usbmodem11301 # for MacOs (/dev/ttyACM0 for Linux)

SRCS := main.s
OBJ := $(SRCS:.s=.o)
ELF := program.elf
HEX := program.hex

all: assemble convert flash

assemble:
	avr-as $(SRCS) -o $(OBJ)
	avr-ld $(OBJ) -o $(ELF)

verify:
	avr-objdump -d $(ELF)

convert:
	avr-objcopy -O ihex $(ELF) $(HEX)

flash:
	avrdude -patmega328p -carduino -P$(PORT) -b115200 -D -Uflash:w:$(HEX):i

clean:
	rm -f *.o *.elf *.hex

.PHONY: all assemble verify convert flash clean

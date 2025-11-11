#include <avr/io.h>
#include <util/delay.h>
#include "uart.h"

int main(void) {
    UART__init();

    while (1) {
		uint8_t c = UART__getc();
		UART__putc(c);
        _delay_ms(100); // Petite pause pour éviter de saturer l'émetteur, et permettre de voir les caractères un par un
    }
}

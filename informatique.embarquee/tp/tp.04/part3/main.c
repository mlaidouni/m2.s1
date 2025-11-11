#include <avr/io.h>
#include <util/delay.h>
#include "uart.h"

int main(void) {
    DDRB |= (1 << PB5); // configure la broche PB5 (LED intégrée) en sortie
    UART__init();

    while (1) {
        UART__getc();
        PORTB |= (1 << PB5); // allume la LED
        _delay_ms(5000);
        PORTB &= ~(1 << PB5); // éteint la LED
		// UART__putc(c); // renvoie le caractère reçu
    }
}

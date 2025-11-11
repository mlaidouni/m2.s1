// slave.c
#include <avr/io.h>
#include "uart.h"

int main(void) {
    // Config PB5 (LED) en sortie
    DDRB |= (1 << PB5);
    PORTB &= ~(1 << PB5); // LED éteinte

    UART__init();

    while (1) {
        uint8_t c = UART__getc(); // non bloquant : retourne 0 si rien
        if (c == 'A') {
            PORTB |= (1 << PB5);  // allume LED
        } else if (c == 'E') {
            PORTB &= ~(1 << PB5); // éteint LED
        }
        // sinon on continue la boucle
    }
}

// master.c
#include <avr/io.h>
#include <util/delay.h>
#include "uart.h"

// Envoi automatique : A puis après 1s E puis 1s A ...
int main(void) {
    UART__init();

    while (1) {
        UART__putc('A');   // demande d'allumer la LED de l'esclave
        _delay_ms(1000);
        UART__putc('E');   // demande d'éteindre la LED de l'esclave
        _delay_ms(1000);
    }
}

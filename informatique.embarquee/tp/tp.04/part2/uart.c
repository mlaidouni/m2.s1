#include <avr/io.h>
#include <stdint.h>
#include "uart.h"

void UART__init(void) {
    uint16_t ubrr = MYUBRR;
    UBRR0H = (uint8_t)(ubrr >> 8);  // bits de poids fort du baud rate (bits 15–8)
    UBRR0L = (uint8_t)ubrr;         // bits de poids faible (bits 7–0)

    UCSR0B = (1 << RXEN0) | (1 << TXEN0);           // Active RX/TX
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);         // 8 bits, 1 stop, pas de parité
}

uint8_t UART__getc(void) {
    while (!(UCSR0A & (1 << RXC0))) ; // attend qu’un octet soit reçu
    return UDR0;                       // lit la donnée reçue
}

void UART__putc(uint8_t data) {
    while (!(UCSR0A & (1 << UDRE0))) ; // attend que le registre soit libre
    UDR0 = data;                        // envoie la donnée
}
